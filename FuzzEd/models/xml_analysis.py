# FuzzEd/models/xml_analysis.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0a49e237d692dded0ce0398c26bf115ddcebf747
# Generated 2013-04-04 22:37:33.508920 by PyXB version 1.2.1
# Namespace net.fuzztree.analysis

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:7a40b0e3-9d67-11e2-81b0-58b035ff3a58')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import xml_fuzztree

Namespace = pyxb.namespace.NamespaceForURI(u'net.fuzztree.analysis', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {net.fuzztree.analysis}AnalysisResult with content type ELEMENT_ONLY
class AnalysisResult_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {net.fuzztree.analysis}AnalysisResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AnalysisResult')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 4, 2)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element errors uses Python identifier errors
    __errors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'errors'), 'errors', '__net_fuzztree_analysis_AnalysisResult__errors', True, pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 6, 6), )

    
    errors = property(__errors.value, __errors.set, None, None)

    
    # Element warnings uses Python identifier warnings
    __warnings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'warnings'), 'warnings', '__net_fuzztree_analysis_AnalysisResult__warnings', True, pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 7, 6), )

    
    warnings = property(__warnings.value, __warnings.set, None, None)

    
    # Element configurations uses Python identifier configurations
    __configurations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configurations'), 'configurations', '__net_fuzztree_analysis_AnalysisResult__configurations', True, pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 8, 6), )

    
    configurations = property(__configurations.value, __configurations.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__net_fuzztree_analysis_AnalysisResult__id', pyxb.binding.datatypes.int)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 10, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 10, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute modelId uses Python identifier modelId
    __modelId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'modelId'), 'modelId', '__net_fuzztree_analysis_AnalysisResult__modelId', pyxb.binding.datatypes.int, required=True)
    __modelId._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 11, 4)
    __modelId._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 11, 4)
    
    modelId = property(__modelId.value, __modelId.set, None, None)

    
    # Attribute timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'timestamp'), 'timestamp', '__net_fuzztree_analysis_AnalysisResult__timestamp', pyxb.binding.datatypes.string, required=True)
    __timestamp._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 12, 4)
    __timestamp._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 12, 4)
    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Attribute validResult uses Python identifier validResult
    __validResult = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'validResult'), 'validResult', '__net_fuzztree_analysis_AnalysisResult__validResult', pyxb.binding.datatypes.boolean, required=True)
    __validResult._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 13, 4)
    __validResult._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 13, 4)
    
    validResult = property(__validResult.value, __validResult.set, None, None)

    
    # Attribute decompositionNumber uses Python identifier decompositionNumber
    __decompositionNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'decompositionNumber'), 'decompositionNumber', '__net_fuzztree_analysis_AnalysisResult__decompositionNumber', pyxb.binding.datatypes.int, required=True)
    __decompositionNumber._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 14, 4)
    __decompositionNumber._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 14, 4)
    
    decompositionNumber = property(__decompositionNumber.value, __decompositionNumber.set, None, None)


    _ElementMap = {
        __errors.name() : __errors,
        __warnings.name() : __warnings,
        __configurations.name() : __configurations
    }
    _AttributeMap = {
        __id.name() : __id,
        __modelId.name() : __modelId,
        __timestamp.name() : __timestamp,
        __validResult.name() : __validResult,
        __decompositionNumber.name() : __decompositionNumber
    }
Namespace.addCategoryObject('typeBinding', u'AnalysisResult', AnalysisResult_)


# Complex type {net.fuzztree.analysis}AnalysisError with content type EMPTY
class AnalysisError_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {net.fuzztree.analysis}AnalysisError with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AnalysisError')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 17, 2)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__net_fuzztree_analysis_AnalysisError__message', pyxb.binding.datatypes.string, required=True)
    __message._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 18, 4)
    __message._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 18, 4)
    
    message = property(__message.value, __message.set, None, None)

    
    # Attribute elementId uses Python identifier elementId
    __elementId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'elementId'), 'elementId', '__net_fuzztree_analysis_AnalysisError__elementId', pyxb.binding.datatypes.int, required=True)
    __elementId._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 19, 4)
    __elementId._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 19, 4)
    
    elementId = property(__elementId.value, __elementId.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __message.name() : __message,
        __elementId.name() : __elementId
    }
Namespace.addCategoryObject('typeBinding', u'AnalysisError', AnalysisError_)


# Complex type {net.fuzztree.analysis}AnalysisWarning with content type EMPTY
class AnalysisWarning_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {net.fuzztree.analysis}AnalysisWarning with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AnalysisWarning')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 22, 2)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__net_fuzztree_analysis_AnalysisWarning__message', pyxb.binding.datatypes.string, required=True)
    __message._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 23, 4)
    __message._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 23, 4)
    
    message = property(__message.value, __message.set, None, None)

    
    # Attribute elementId uses Python identifier elementId
    __elementId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'elementId'), 'elementId', '__net_fuzztree_analysis_AnalysisWarning__elementId', pyxb.binding.datatypes.int, required=True)
    __elementId._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 24, 4)
    __elementId._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 24, 4)
    
    elementId = property(__elementId.value, __elementId.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __message.name() : __message,
        __elementId.name() : __elementId
    }
Namespace.addCategoryObject('typeBinding', u'AnalysisWarning', AnalysisWarning_)


# Complex type {net.fuzztree.analysis}Configuration with content type ELEMENT_ONLY
class Configuration_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {net.fuzztree.analysis}Configuration with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Configuration')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 27, 2)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element choices uses Python identifier choices
    __choices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'choices'), 'choices', '__net_fuzztree_analysis_Configuration__choices', True, pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 29, 6), )

    
    choices = property(__choices.value, __choices.set, None, None)

    
    # Element probability uses Python identifier probability
    __probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'probability'), 'probability', '__net_fuzztree_analysis_Configuration__probability', False, pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 30, 6), )

    
    probability = property(__probability.value, __probability.set, None, None)

    
    # Attribute costs uses Python identifier costs
    __costs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'costs'), 'costs', '__net_fuzztree_analysis_Configuration__costs', pyxb.binding.datatypes.int, required=True)
    __costs._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 32, 4)
    __costs._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 32, 4)
    
    costs = property(__costs.value, __costs.set, None, None)


    _ElementMap = {
        __choices.name() : __choices,
        __probability.name() : __probability
    }
    _AttributeMap = {
        __costs.name() : __costs
    }
Namespace.addCategoryObject('typeBinding', u'Configuration', Configuration_)


# Complex type {net.fuzztree.analysis}Choice with content type EMPTY
class Choice (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {net.fuzztree.analysis}Choice with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Choice')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 35, 2)
    # Base type is pyxb.binding.datatypes.anyType

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'Choice', Choice)


# Complex type {net.fuzztree.analysis}IntegerToChoiceMap with content type ELEMENT_ONLY
class IntegerToChoiceMap_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {net.fuzztree.analysis}IntegerToChoiceMap with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IntegerToChoiceMap')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 71, 2)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__net_fuzztree_analysis_IntegerToChoiceMap__value', False, pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 73, 6), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'key'), 'key', '__net_fuzztree_analysis_IntegerToChoiceMap__key', pyxb.binding.datatypes.int, required=True)
    __key._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 75, 4)
    __key._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 75, 4)
    
    key = property(__key.value, __key.set, None, None)


    _ElementMap = {
        __value.name() : __value
    }
    _AttributeMap = {
        __key.name() : __key
    }
Namespace.addCategoryObject('typeBinding', u'IntegerToChoiceMap', IntegerToChoiceMap_)


# Complex type {net.fuzztree.analysis}InclusionChoice with content type EMPTY
class InclusionChoice_ (Choice):
    """Complex type {net.fuzztree.analysis}InclusionChoice with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'InclusionChoice')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 36, 2)
    # Base type is Choice
    
    # Attribute included uses Python identifier included
    __included = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'included'), 'included', '__net_fuzztree_analysis_InclusionChoice__included', pyxb.binding.datatypes.boolean, required=True)
    __included._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 39, 8)
    __included._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 39, 8)
    
    included = property(__included.value, __included.set, None, None)


    _ElementMap = Choice._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Choice._AttributeMap.copy()
    _AttributeMap.update({
        __included.name() : __included
    })
Namespace.addCategoryObject('typeBinding', u'InclusionChoice', InclusionChoice_)


# Complex type {net.fuzztree.analysis}RedundancyChoice with content type EMPTY
class RedundancyChoice_ (Choice):
    """Complex type {net.fuzztree.analysis}RedundancyChoice with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RedundancyChoice')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 44, 2)
    # Base type is Choice
    
    # Attribute n uses Python identifier n
    __n = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'n'), 'n', '__net_fuzztree_analysis_RedundancyChoice__n', pyxb.binding.datatypes.int, required=True)
    __n._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 47, 8)
    __n._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 47, 8)
    
    n = property(__n.value, __n.set, None, None)


    _ElementMap = Choice._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Choice._AttributeMap.copy()
    _AttributeMap.update({
        __n.name() : __n
    })
Namespace.addCategoryObject('typeBinding', u'RedundancyChoice', RedundancyChoice_)


# Complex type {net.fuzztree.analysis}FeatureChoice with content type EMPTY
class FeatureChoice_ (Choice):
    """Complex type {net.fuzztree.analysis}FeatureChoice with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FeatureChoice')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 52, 2)
    # Base type is Choice
    
    # Attribute featureId uses Python identifier featureId
    __featureId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'featureId'), 'featureId', '__net_fuzztree_analysis_FeatureChoice__featureId', pyxb.binding.datatypes.int, required=True)
    __featureId._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 55, 8)
    __featureId._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 55, 8)
    
    featureId = property(__featureId.value, __featureId.set, None, None)


    _ElementMap = Choice._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Choice._AttributeMap.copy()
    _AttributeMap.update({
        __featureId.name() : __featureId
    })
Namespace.addCategoryObject('typeBinding', u'FeatureChoice', FeatureChoice_)


# Complex type {net.fuzztree.analysis}ConfigurationInstance with content type ELEMENT_ONLY
class ConfigurationInstance_ (xml_fuzztree.Annotation):
    """Complex type {net.fuzztree.analysis}ConfigurationInstance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ConfigurationInstance')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 60, 2)
    # Base type is xml_fuzztree.Annotation
    
    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'configuration'), 'configuration', '__net_fuzztree_analysis_ConfigurationInstance__configuration', False, pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 64, 10), )

    
    configuration = property(__configuration.value, __configuration.set, None, None)

    
    # Attribute ancestorModelId uses Python identifier ancestorModelId
    __ancestorModelId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ancestorModelId'), 'ancestorModelId', '__net_fuzztree_analysis_ConfigurationInstance__ancestorModelId', pyxb.binding.datatypes.int, required=True)
    __ancestorModelId._DeclarationLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 66, 8)
    __ancestorModelId._UseLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 66, 8)
    
    ancestorModelId = property(__ancestorModelId.value, __ancestorModelId.set, None, None)


    _ElementMap = xml_fuzztree.Annotation._ElementMap.copy()
    _ElementMap.update({
        __configuration.name() : __configuration
    })
    _AttributeMap = xml_fuzztree.Annotation._AttributeMap.copy()
    _AttributeMap.update({
        __ancestorModelId.name() : __ancestorModelId
    })
Namespace.addCategoryObject('typeBinding', u'ConfigurationInstance', ConfigurationInstance_)


# Complex type {net.fuzztree.analysis}TransferInResult with content type ELEMENT_ONLY
class TransferInResult_ (xml_fuzztree.Annotation):
    """Complex type {net.fuzztree.analysis}TransferInResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TransferInResult')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 78, 2)
    # Base type is xml_fuzztree.Annotation
    
    # Element analysisResult uses Python identifier analysisResult
    __analysisResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'analysisResult'), 'analysisResult', '__net_fuzztree_analysis_TransferInResult__analysisResult', False, pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 82, 10), )

    
    analysisResult = property(__analysisResult.value, __analysisResult.set, None, None)


    _ElementMap = xml_fuzztree.Annotation._ElementMap.copy()
    _ElementMap.update({
        __analysisResult.name() : __analysisResult
    })
    _AttributeMap = xml_fuzztree.Annotation._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'TransferInResult', TransferInResult_)


# Complex type {net.fuzztree.analysis}TransferInChoice with content type ELEMENT_ONLY
class TransferInChoice_ (Choice):
    """Complex type {net.fuzztree.analysis}TransferInChoice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TransferInChoice')
    _XSDLocation = pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 88, 2)
    # Base type is Choice
    
    # Element chosenConfiguration uses Python identifier chosenConfiguration
    __chosenConfiguration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'chosenConfiguration'), 'chosenConfiguration', '__net_fuzztree_analysis_TransferInChoice__chosenConfiguration', False, pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 92, 10), )

    
    chosenConfiguration = property(__chosenConfiguration.value, __chosenConfiguration.set, None, None)


    _ElementMap = Choice._ElementMap.copy()
    _ElementMap.update({
        __chosenConfiguration.name() : __chosenConfiguration
    })
    _AttributeMap = Choice._AttributeMap.copy()
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'TransferInChoice', TransferInChoice_)


AnalysisResult = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AnalysisResult'), AnalysisResult_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 16, 2))
Namespace.addCategoryObject('elementBinding', AnalysisResult.name().localName(), AnalysisResult)

AnalysisError = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AnalysisError'), AnalysisError_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 21, 2))
Namespace.addCategoryObject('elementBinding', AnalysisError.name().localName(), AnalysisError)

AnalysisWarning = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AnalysisWarning'), AnalysisWarning_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 26, 2))
Namespace.addCategoryObject('elementBinding', AnalysisWarning.name().localName(), AnalysisWarning)

Configuration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Configuration'), Configuration_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 34, 2))
Namespace.addCategoryObject('elementBinding', Configuration.name().localName(), Configuration)

IntegerToChoiceMap = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IntegerToChoiceMap'), IntegerToChoiceMap_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 77, 2))
Namespace.addCategoryObject('elementBinding', IntegerToChoiceMap.name().localName(), IntegerToChoiceMap)

InclusionChoice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InclusionChoice'), InclusionChoice_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 43, 2))
Namespace.addCategoryObject('elementBinding', InclusionChoice.name().localName(), InclusionChoice)

RedundancyChoice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RedundancyChoice'), RedundancyChoice_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 51, 2))
Namespace.addCategoryObject('elementBinding', RedundancyChoice.name().localName(), RedundancyChoice)

FeatureChoice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FeatureChoice'), FeatureChoice_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 59, 2))
Namespace.addCategoryObject('elementBinding', FeatureChoice.name().localName(), FeatureChoice)

ConfigurationInstance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConfigurationInstance'), ConfigurationInstance_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 70, 2))
Namespace.addCategoryObject('elementBinding', ConfigurationInstance.name().localName(), ConfigurationInstance)

TransferInResult = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransferInResult'), TransferInResult_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 87, 2))
Namespace.addCategoryObject('elementBinding', TransferInResult.name().localName(), TransferInResult)

TransferInChoice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransferInChoice'), TransferInChoice_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 97, 2))
Namespace.addCategoryObject('elementBinding', TransferInChoice.name().localName(), TransferInChoice)



AnalysisResult_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'errors'), AnalysisError_, scope=AnalysisResult_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 6, 6)))

AnalysisResult_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'warnings'), AnalysisWarning_, scope=AnalysisResult_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 7, 6)))

AnalysisResult_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configurations'), Configuration_, scope=AnalysisResult_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 8, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 6, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 7, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 8, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnalysisResult_._UseForTag(pyxb.namespace.ExpandedName(None, u'errors')), pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 6, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AnalysisResult_._UseForTag(pyxb.namespace.ExpandedName(None, u'warnings')), pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 7, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AnalysisResult_._UseForTag(pyxb.namespace.ExpandedName(None, u'configurations')), pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 8, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AnalysisResult_._Automaton = _BuildAutomaton()




Configuration_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'choices'), IntegerToChoiceMap_, scope=Configuration_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 29, 6)))

Configuration_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'probability'), xml_fuzztree.DecomposedFuzzyProbability_, scope=Configuration_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 30, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 29, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 30, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Configuration_._UseForTag(pyxb.namespace.ExpandedName(None, u'choices')), pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 29, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Configuration_._UseForTag(pyxb.namespace.ExpandedName(None, u'probability')), pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 30, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Configuration_._Automaton = _BuildAutomaton_()




IntegerToChoiceMap_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'value'), Choice, scope=IntegerToChoiceMap_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 73, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IntegerToChoiceMap_._UseForTag(pyxb.namespace.ExpandedName(None, u'value')), pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 73, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
IntegerToChoiceMap_._Automaton = _BuildAutomaton_2()




ConfigurationInstance_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'configuration'), Configuration_, scope=ConfigurationInstance_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 64, 10)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConfigurationInstance_._UseForTag(pyxb.namespace.ExpandedName(None, u'configuration')), pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 64, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConfigurationInstance_._Automaton = _BuildAutomaton_3()




TransferInResult_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'analysisResult'), AnalysisResult_, scope=TransferInResult_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 82, 10)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransferInResult_._UseForTag(pyxb.namespace.ExpandedName(None, u'analysisResult')), pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 82, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TransferInResult_._Automaton = _BuildAutomaton_4()




TransferInChoice_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'chosenConfiguration'), Configuration_, scope=TransferInChoice_, location=pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 92, 10)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransferInChoice_._UseForTag(pyxb.namespace.ExpandedName(None, u'chosenConfiguration')), pyxb.utils.utility.Location('/Users/troeger/svn/fuzztrees/FuzzEd/static/xsd/analysis.xsd', 92, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TransferInChoice_._Automaton = _BuildAutomaton_5()

