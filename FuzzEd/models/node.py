from django.core.exceptions import ObjectDoesNotExist

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

import logging
logger = logging.getLogger('FuzzEd')

import xml_fuzztree
import xml_faulttree
from graph import Graph

import json, notations, sys, time

def new_client_id():
    return str(int(time.mktime(time.gmtime())))

fuzztree_classes = {
    'topEvent':             xml_fuzztree.TopEvent,
    'basicEvent':           xml_fuzztree.BasicEvent,
    'basicEventSet':        xml_fuzztree.BasicEventSet,
    'intermediateEvent':    xml_fuzztree.IntermediateEvent,
    'intermediateEventSet': xml_fuzztree.IntermediateEventSet,
    'houseEvent':           xml_fuzztree.HouseEvent,
    'undevelopedEvent':     xml_fuzztree.UndevelopedEvent,
    'andGate':              xml_fuzztree.And,
    'orGate':               xml_fuzztree.Or,
    'xorGate':              xml_fuzztree.Xor,
    'votingOrGate':         xml_fuzztree.VotingOr,
    'featureVariation':     xml_fuzztree.FeatureVariationPoint,
    'redundancyVariation':  xml_fuzztree.RedundancyVariationPoint,
    'transferIn':           xml_fuzztree.TransferIn
}

faulttree_classes = {
    'topEvent':             xml_faulttree.TopEvent,
    'basicEvent':           xml_faulttree.BasicEvent,
    'basicEventSet':        xml_faulttree.BasicEventSet,
    'intermediateEvent':    xml_faulttree.IntermediateEvent,
    'intermediateEventSet': xml_faulttree.IntermediateEventSet,    
    'houseEvent':           xml_faulttree.HouseEvent,
    'undevelopedEvent':     xml_faulttree.UndevelopedEvent,
    'andGate':              xml_faulttree.And,
    'orGate':               xml_faulttree.Or,
    'xorGate':              xml_faulttree.Xor,
    'votingOrGate':         xml_faulttree.VotingOr,
    'transferIn':           xml_faulttree.TransferIn
}

class Node(models.Model):
    """
    Class: Node

    This class models a generic node for any diagram notation.

    Fields:
     {long}    client_id - an id for this node that is generated by the client
     {str}     kind      - a unique identifier for the kind of the node in its notation - e.g. "choice" for FuzzTrees.
                           Must be in the set of available node kinds of the owning graph's notation
     {<Graph>} graph     - the graph that owns the node
     {int}     x         - the x coordinate of the node (default: 0)
     {int}     y         - the y coordinate of the node (default: 0) 
     {bool}    deleted   - flag indicating whether this node is deleted. Simplifies restoration of nodes by toggling
                           the flag (default: False)
    """
    class Meta:
        app_label = 'FuzzEd'

    # Nodes that are created by the server (e.g. default nodes in the notation) should receive ids starting at
    # -sys.maxint and autoincrement from there on. The whole negative number range is reserved for the server. IDs from
    # the client MUST be zero or greater (usually UNIX timestamp in milliseconds from JS)
    client_id = models.BigIntegerField(default=-sys.maxint)
    kind      = models.CharField(max_length=127, choices=notations.node_choices)
    graph     = models.ForeignKey(Graph, null=False, related_name='nodes')
    x         = models.IntegerField(default=0)
    y         = models.IntegerField(default=0)
    deleted   = models.BooleanField(default=False)

    def __unicode__(self):
        prefix = '[DELETED] ' if self.deleted else ''

        try:
            name = unicode(self.properties.get(key='name').value)
            return unicode('%s%s' % (prefix, name))

        except ObjectDoesNotExist:
            return unicode('%s%s_%s' % (prefix, self.pk, notations.by_kind[self.graph.kind]['nodes'][self.kind]['properties']['name']['default']))

    def to_json(self):
        """
        Method: to_json
        
        Serializes the values of this node into JSON notation.

        Returns:
         {str} the node in JSON representation
        """
        return json.dumps(self.to_dict())

    def to_dict(self):
        """
        Method: to_dict
        
        Serializes this node into a native dictionary
        
        Returns:
         {dict} the node as dictionary
        """
        return {
            'properties': {prop.key: {'value': prop.value} for prop in self.properties.filter(deleted=False)},
            'id':         self.client_id,
            'kind':       self.kind,
            'x':          self.x,
            'y':          self.y,
            'outgoing':   [edge.client_id for edge in self.outgoing.filter(deleted=False)],
            'incoming':   [edge.client_id for edge in self.incoming.filter(deleted=False)]
        }

    def to_bool_term(self):
        edges = self.outgoing.filter(deleted=False).all()
        children = []

        for edge in edges:
            children.append(edge.target.to_bool_term())

        if self.kind == 'orGate':
            return '(%s)' % (' or '.join(children))

        elif self.kind == 'andGate':
            return '(%s)' % (' and '.join(children))

        elif self.kind in {'basicEvent'}:
            return str(self.client_id)

        elif self.kind == 'topEvent':
            return str(children[0])

        raise ValueError('Node %s has unsupported kind' % self)

    def get_all_mirror_properties(self, hiddenProps=[]):
        """
        Returns a sorted set of all node properties and their values, according to the notation rendering rules.
        """
        result = []
        # Only consider properties that have to be displayed in the mirror 
        displayOrder = notations.by_kind[self.graph.kind]['propertiesDisplayOrder']
        propdetails = notations.by_kind[self.graph.kind]['nodes'][self.kind]['properties']
        for prop in displayOrder:
            if propdetails.has_key(prop) and prop not in hiddenProps:   # the displayOrder list is static, the property does not have to be part of this node
                val = self.get_property(prop, None)
                if isinstance(propdetails[prop],dict):          # Some properties do not have a config dict in notations, such as optional=None
                    kind = propdetails[prop]['kind']
                else:
                    logger.debug("Property %s in %s has no config dictionary"%(prop, self.kind))
                    kind="text"
                if val != None:
                    if kind == "range":
                        format = propdetails[prop]['mirror']['format']
                        format = format.replace(u"\xb1","$\\pm$")    # Special unicodes used in format strings, such as \xb1
                        val = format.replace("{{$0}}",str(val[0])).replace("{{$1}}",str(val[1]))
                    elif kind == "compound":
                        active_part = val[0]    # Compounds are unions, the first number tells us the active part defintion
                        partkind = propdetails[prop]['parts'][active_part]['kind']
                        format =   propdetails[prop]['parts'][active_part]['mirror']['format']
                        format = format.replace(u"\xb1","$\\pm$")    # Special unicodes used in format strings, such as \xb1
                        if partkind == 'epsilon': 
                            val = format.replace("{{$0}}",str(val[1][0])).replace("{{$1}}",str(val[1][1]))
                        elif partkind == 'choice':
                            val = format.replace("{{$0}}",str(val[1][0]))
                    elif propdetails[prop].has_key('mirror'):
                        if propdetails[prop]['mirror'].has_key('format'):
                            val = propdetails[prop]['mirror']['format'].replace("{{$0}}",str(val))
                        else:
                            val = str(val)
                    else:
                        # Property has no special type and no mirror definition, so it shouldn't be shown
                        # One example is the name of the top event
                        continue
                    result.append(val)
        return result


    def to_tikz(self, x_offset=0, y_offset=0, parent_kind=None):
        """
        Serializes this node and all its children into a TiKZ representation.
        A positive x offset shifts the resulting tree accordingly to the right.
        Negative offsets are allowed.

        We are intentionally do not use the TiKZ tree rendering capabilities, since this
        would ignore all user formatting of the tree from the editor.

        TikZ starts the coordinate system in the upper left corner, while we start in the lower left corner.
        This demands some coordinate mangling on the Y axis.

        Returns:
         {str} the node and its children in LaTex representation
        """
        nodekind = self.kind.lower()
        # Optional nodes are dashed
        if self.get_property("optional", False):
            nodeStyle = "shapeStyleDashed"
        else:
            nodeStyle = "shapeStyle"     
        # If this is a child node, we need to check if the parent wants to hide some child property
        hiddenProps = []
        if parent_kind:
            nodeConfig = notations.by_kind[self.graph.kind]['nodes'][parent_kind]
            if nodeConfig.has_key('childProperties'):
                for childPropName in nodeConfig['childProperties']:
                    for childPropSettingName, childPropSettingVal in nodeConfig['childProperties'][childPropName].iteritems():
                        if childPropSettingName == "hidden" and childPropSettingVal == True:
                            hiddenProps.append(childPropName)
        # Create Tikz snippet for tree node, we start with the TiKZ node for the graph icon
        # Y coordinates are stretched a little bit, for optics
        result = "\\node [shape=%s, %s] at (%u, -%f) (%u) {};\n"%(self.kind, nodeStyle, self.x+x_offset, (self.y+y_offset)*1.2, self.pk)
        # Determine the mirror text based on all properties
        # Text width is exactly the double width of the icons
        mirrorText = ""
        for index,propvalue in enumerate(self.get_all_mirror_properties(hiddenProps)):
            propvalue = propvalue.replace("#","\\#")    # consider special LaTex character in mirror text
            if index==0:
                # Make the first property bigger, since it is supposed to be the name
                propvalue = "\\baselineskip=0.8\\baselineskip\\textbf{{\\footnotesize %s}}"%propvalue  
            else:
                propvalue = "{\\it\\scriptsize %s}"%propvalue                                
            mirrorText += "%s\\\\"%propvalue
        # Create child nodes and their edges
        for edge in self.outgoing.filter(deleted=False):
            # Add child node rendering
            result += edge.target.to_tikz(x_offset, y_offset, self.kind)
            # Add connector from this node to the added child, consider if dashed line is needed
            if notations.by_kind[self.graph.kind]['nodes'][self.kind]['connector'].has_key('dashstyle'):
                result += "\path[fork edge, dashed] (%s.south) edge (%u.north);\n"%(self.pk, edge.target.pk)
            else:
                result += "\path[fork edge] (%s.south) edge (%u.north);\n"%(self.pk, edge.target.pk)
        # Add the mirror text as separate text node, which makes formatting more precise
        if mirrorText != "":
            result += "\\node [mirrorStyle] at (%u.south) (text%u) {%s};\n"%(self.pk, self.pk, mirrorText)
        return result

    def to_xml(self, xmltype=None):
        """
        Method: to_xml
        
        Serializes this node into an XML representation according to the schema file for the graph type. Please note
        the backend node ID is used instead of client_id, since the latter one is not globally unique and may be too
        long for some XML processors.
        
        Returns:
         The XML node instance for this graph node and its children
        """

        # If the target XML type is not given, we take the graph type
        if not xmltype:
            xmltype = self.graph.kind

        properties = {
            'id':   self.id,
            'name': self.get_property('name', '-')
        }

        if self.kind == 'transferIn':
            properties['fromModelId'] = self.get_property('transfer')

        # for any node that may have a quantity, set the according property
        if self.kind in {'basicEventSet', 'intermediateEventSet'}:
            properties['quantity'] = self.get_property('cardinality')

        # Special treatment for some of the FuzzTree node types
        if xmltype == 'fuzztree':
            # for any node that may be optional, set the according property
            if self.kind in {'basicEvent', 'basicEventSet', 'intermediateEvent', 'intermediateEventSet', 'houseEvent'}:
                properties['optional'] = self.get_property('optional', False)

            # determine fuzzy or crisp probability, set it accordingly
            if self.kind in {'basicEvent', 'basicEventSet', 'houseEvent'}:
                probability = self.get_property('probability', None)
                if isinstance(probability, list):
                    point = probability[-1][0]
                    alpha = probability[-1][1]

                    print probability, point, alpha

                    if alpha == 0:
                        properties['probability'] = xml_fuzztree.CrispProbability(value_=point)
                    else:
                        properties['probability'] = xml_fuzztree.TriangularFuzzyInterval(
                            a=point - alpha, b1=point, b2=point, c=point + alpha
                        )
                elif isinstance(probability, (long, int, float)):
                    properties['probability'] = xml_fuzztree.CrispProbability(value_=probability)
                else:
                    raise ValueError('Cannot handle probability value: "%s"' % probability)
                # nodes that have a probability also have costs in FuzzTrees
                properties['costs'] = self.get_property('cost', 0)

            # Voting OR in FuzzTrees has different parameter name than in fault trees
            elif self.kind == 'votingOrGate':
                properties['k'] = self.get_property('k')

            # add range attribute for redundancy variation
            elif self.kind == 'redundancyVariation':
                nRange = self.get_property('nRange')
                properties['start']   = nRange[0]
                properties['end']     = nRange[1]
                properties['formula'] = self.get_property('kFormula')

            xml_node = fuzztree_classes[self.kind](**properties)

        # Special treatment for some of the FaultTree node types
        elif xmltype == 'faulttree':
            if self.kind == 'votingOrGate':
                properties['k'] = self.get_property('k')

            # determine fuzzy or crisp probability, set it accordingly
            if self.kind in {'basicEvent', 'basicEventSet', 'houseEvent'}:
                properties['probability'] = xml_faulttree.CrispProbability(value_=self.get_property('probability', None))

            xml_node = faulttree_classes[self.kind](**properties)

        # serialize children
        logger.debug('[XML] Added node "%s" with properties %s' % (self.kind, properties))
        for edge in self.outgoing.filter(deleted=False):
            xml_node.children.append(edge.target.to_xml(xmltype))

        return xml_node

    def get_property(self, key, default=None):
        try:
            return self.properties.get(key=key).value
        except ObjectDoesNotExist:
            try:
                logger.debug('[XML] Node has no property "%s", trying to use default from notation' % key)
                return notations.by_kind[self.graph.kind]['nodes'][self.kind]['properties'][key]['default']
            except KeyError:
                logger.debug('[XML] No default given in notation, assuming "%s" instead' % default)
                return default

    def get_attr(self, key):
        """
        Method: get_attr

        Use this method to fetch a node's attribute. It looks in the node object and its related properties.

        Parameters:
            {string} key - The name of the attribute.

        Returns:
            {attr} The found attribute. Raises a ValueError if no attribute for the given key exist.
        """
        if hasattr(self, key):
            return getattr(self, key)
        else:
            try:
                prop = self.properties.get(key=key)
                return prop.value
            except Exception:
                raise ValueError()

    def set_attr(self, key, value):
        """
        Method: set_attr

        Use this method to set a node's attribute. It looks in the node object and its related properties for an
        attribute with the given name and changes it. If non exist, a new property is added saving this attribute.

        Parameters:
            {string} key - The name of the attribute.
            {attr} value - The new value that should be stored.
        """
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            prop, created = self.properties.get_or_create(key=key)
            prop.value = value
            prop.save()

# the handler will ensure that the kind of the node is present in its containing graph notation
@receiver(pre_save, sender=Node)
def validate(sender, instance, raw, **kwargs):
    # raw is true if fixture loading happens, where the graph does not exist so far
    if not raw:
        graph = instance.graph
        if not instance.kind in notations.by_kind[graph.kind]['nodes']:
            raise ValueError('Graph %s does not support nodes of type %s' % (graph, instance.kind))

# ensures that the validate handler is not exported
__all__ = ['Node']
