// Copyright (C) 2005-2010 Code Synthesis Tools CC
//
// This program was generated by CodeSynthesis XSD, an XML Schema to
// C++ data binding compiler.
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License version 2 as
// published by the Free Software Foundation.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
//
// In addition, as a special exception, Code Synthesis Tools CC gives
// permission to link this program with the Xerces-C++ library (or with
// modified versions of Xerces-C++ that use the same license as Xerces-C++),
// and distribute linked combinations including the two. You must obey
// the GNU General Public License version 2 in all respects for all of
// the code used other than Xerces-C++. If you modify this copy of the
// program, you may extend this exception to your version of the program,
// but you are not obligated to do so. If you do not wish to do so, delete
// this exception statement from your version.
//
// Furthermore, Code Synthesis Tools CC makes a special exception for
// the Free/Libre and Open Source Software (FLOSS) which is described
// in the accompanying FLOSSE file.
//

#ifndef C__DEV_FUZZTREES_FUZZTREECONFIGURATION_XML_FAULTTREE_H
#define C__DEV_FUZZTREES_FUZZTREECONFIGURATION_XML_FAULTTREE_H

// Begin prologue.
//
//
// End prologue.

#include <xsd/cxx/config.hxx>

#if (XSD_INT_VERSION != 3030000L)
#error XSD runtime version mismatch
#endif

#include <xsd/cxx/pre.hxx>

#include <faulttree-fwd.hxx>

#include <memory>    // std::auto_ptr
#include <limits>    // std::numeric_limits
#include <algorithm> // std::binary_search

#include <xsd/cxx/xml/char-utf8.hxx>

#include <xsd/cxx/tree/exceptions.hxx>
#include <xsd/cxx/tree/elements.hxx>
#include <xsd/cxx/tree/containers.hxx>
#include <xsd/cxx/tree/list.hxx>

#include <xsd/cxx/xml/dom/parsing-header.hxx>

namespace faulttree
{
  class Annotation: public ::xml_schema::Type
  {
    public:
    // Constructors.
    //
    Annotation ();

    Annotation (const ::xercesc::DOMElement& e,
                ::xml_schema::Flags f = 0,
                ::xml_schema::Container* c = 0);

    Annotation (const ::xercesc::DOMAttr& a,
                ::xml_schema::Flags f = 0,
                ::xml_schema::Container* c = 0);

    Annotation (const ::std::string& s,
                const ::xercesc::DOMElement* e,
                ::xml_schema::Flags f = 0,
                ::xml_schema::Container* c = 0);

    Annotation (const Annotation& x,
                ::xml_schema::Flags f = 0,
                ::xml_schema::Container* c = 0);

    virtual Annotation*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~Annotation ();
  };

  class Probability: public ::xml_schema::Type
  {
    public:
    // Constructors.
    //
    Probability ();

    Probability (const ::xercesc::DOMElement& e,
                 ::xml_schema::Flags f = 0,
                 ::xml_schema::Container* c = 0);

    Probability (const ::xercesc::DOMAttr& a,
                 ::xml_schema::Flags f = 0,
                 ::xml_schema::Container* c = 0);

    Probability (const ::std::string& s,
                 const ::xercesc::DOMElement* e,
                 ::xml_schema::Flags f = 0,
                 ::xml_schema::Container* c = 0);

    Probability (const Probability& x,
                 ::xml_schema::Flags f = 0,
                 ::xml_schema::Container* c = 0);

    virtual Probability*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~Probability ();
  };

  class AnnotatedElement: public ::xml_schema::Type
  {
    public:
    // annotations
    // 
    typedef ::faulttree::Annotation AnnotationsType;
    typedef ::xsd::cxx::tree::sequence< AnnotationsType > AnnotationsSequence;
    typedef AnnotationsSequence::iterator AnnotationsIterator;
    typedef AnnotationsSequence::const_iterator AnnotationsConstIterator;
    typedef ::xsd::cxx::tree::traits< AnnotationsType, char > AnnotationsTraits;

    const AnnotationsSequence&
    annotations () const;

    AnnotationsSequence&
    annotations ();

    void
    annotations (const AnnotationsSequence& s);

    // id
    // 
    typedef ::xml_schema::String IdType;
    typedef ::xsd::cxx::tree::traits< IdType, char > IdTraits;

    const IdType&
    id () const;

    IdType&
    id ();

    void
    id (const IdType& x);

    void
    id (::std::auto_ptr< IdType > p);

    // name
    // 
    typedef ::xml_schema::String NameType;
    typedef ::xsd::cxx::tree::optional< NameType > NameOptional;
    typedef ::xsd::cxx::tree::traits< NameType, char > NameTraits;

    const NameOptional&
    name () const;

    NameOptional&
    name ();

    void
    name (const NameType& x);

    void
    name (const NameOptional& x);

    void
    name (::std::auto_ptr< NameType > p);

    // Constructors.
    //
    AnnotatedElement (const IdType&);

    AnnotatedElement (const ::xercesc::DOMElement& e,
                      ::xml_schema::Flags f = 0,
                      ::xml_schema::Container* c = 0);

    AnnotatedElement (const AnnotatedElement& x,
                      ::xml_schema::Flags f = 0,
                      ::xml_schema::Container* c = 0);

    virtual AnnotatedElement*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~AnnotatedElement ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    AnnotationsSequence annotations_;
    ::xsd::cxx::tree::one< IdType > id_;
    NameOptional name_;
  };

  class Model: public ::faulttree::AnnotatedElement
  {
    public:
    // Constructors.
    //
    Model (const IdType&);

    Model (const ::xercesc::DOMElement& e,
           ::xml_schema::Flags f = 0,
           ::xml_schema::Container* c = 0);

    Model (const Model& x,
           ::xml_schema::Flags f = 0,
           ::xml_schema::Container* c = 0);

    virtual Model*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~Model ();
  };

  class Node_base: public ::faulttree::AnnotatedElement
  {
    public:
    // children
    // 
    typedef ::faulttree::ChildNode ChildrenType;
    typedef ::xsd::cxx::tree::sequence< ChildrenType > ChildrenSequence;
    typedef ChildrenSequence::iterator ChildrenIterator;
    typedef ChildrenSequence::const_iterator ChildrenConstIterator;
    typedef ::xsd::cxx::tree::traits< ChildrenType, char > ChildrenTraits;

    const ChildrenSequence&
    children () const;

    ChildrenSequence&
    children ();

    void
    children (const ChildrenSequence& s);

    // x
    // 
    typedef ::xml_schema::Int XType;
    typedef ::xsd::cxx::tree::optional< XType > XOptional;
    typedef ::xsd::cxx::tree::traits< XType, char > XTraits;

    const XOptional&
    x () const;

    XOptional&
    x ();

    void
    x (const XType& x);

    void
    x (const XOptional& x);

    // y
    // 
    typedef ::xml_schema::Int YType;
    typedef ::xsd::cxx::tree::optional< YType > YOptional;
    typedef ::xsd::cxx::tree::traits< YType, char > YTraits;

    const YOptional&
    y () const;

    YOptional&
    y ();

    void
    y (const YType& x);

    void
    y (const YOptional& x);

    // Constructors.
    //
    Node_base (const IdType&);

    Node_base (const ::xercesc::DOMElement& e,
               ::xml_schema::Flags f = 0,
               ::xml_schema::Container* c = 0);

    Node_base (const Node_base& x,
               ::xml_schema::Flags f = 0,
               ::xml_schema::Container* c = 0);

    virtual Node_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~Node_base ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ChildrenSequence children_;
    XOptional x_;
    YOptional y_;
  };

  class ChildNode_base: public ::faulttree::Node
  {
    public:
    // Constructors.
    //
    ChildNode_base (const IdType&);

    ChildNode_base (const ::xercesc::DOMElement& e,
                    ::xml_schema::Flags f = 0,
                    ::xml_schema::Container* c = 0);

    ChildNode_base (const ChildNode_base& x,
                    ::xml_schema::Flags f = 0,
                    ::xml_schema::Container* c = 0);

    virtual ChildNode_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~ChildNode_base ();
  };

  class FaultTree: public ::faulttree::Model
  {
    public:
    // topEvent
    // 
    typedef ::faulttree::TopEvent TopEventType;
    typedef ::xsd::cxx::tree::traits< TopEventType, char > TopEventTraits;

    const TopEventType&
    topEvent () const;

    TopEventType&
    topEvent ();

    void
    topEvent (const TopEventType& x);

    void
    topEvent (::std::auto_ptr< TopEventType > p);

    // Constructors.
    //
    FaultTree (const IdType&,
               const TopEventType&);

    FaultTree (const IdType&,
               ::std::auto_ptr< TopEventType >&);

    FaultTree (const ::xercesc::DOMElement& e,
               ::xml_schema::Flags f = 0,
               ::xml_schema::Container* c = 0);

    FaultTree (const FaultTree& x,
               ::xml_schema::Flags f = 0,
               ::xml_schema::Container* c = 0);

    virtual FaultTree*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~FaultTree ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< TopEventType > topEvent_;
  };

  class TopEvent_base: public ::faulttree::Node
  {
    public:
    // missionTime
    // 
    typedef ::xml_schema::Int MissionTimeType;
    typedef ::xsd::cxx::tree::traits< MissionTimeType, char > MissionTimeTraits;

    const MissionTimeType&
    missionTime () const;

    MissionTimeType&
    missionTime ();

    void
    missionTime (const MissionTimeType& x);

    // Constructors.
    //
    TopEvent_base (const IdType&,
                   const MissionTimeType&);

    TopEvent_base (const ::xercesc::DOMElement& e,
                   ::xml_schema::Flags f = 0,
                   ::xml_schema::Container* c = 0);

    TopEvent_base (const TopEvent_base& x,
                   ::xml_schema::Flags f = 0,
                   ::xml_schema::Container* c = 0);

    virtual TopEvent_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~TopEvent_base ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< MissionTimeType > missionTime_;
  };

  class CrispProbability: public ::faulttree::Probability
  {
    public:
    // value
    // 
    typedef ::xml_schema::Double ValueType;
    typedef ::xsd::cxx::tree::traits< ValueType, char, ::xsd::cxx::tree::schema_type::double_ > ValueTraits;

    const ValueType&
    value () const;

    ValueType&
    value ();

    void
    value (const ValueType& x);

    // Constructors.
    //
    CrispProbability (const ValueType&);

    CrispProbability (const ::xercesc::DOMElement& e,
                      ::xml_schema::Flags f = 0,
                      ::xml_schema::Container* c = 0);

    CrispProbability (const CrispProbability& x,
                      ::xml_schema::Flags f = 0,
                      ::xml_schema::Container* c = 0);

    virtual CrispProbability*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~CrispProbability ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< ValueType > value_;
  };

  class FailureRate: public ::faulttree::Probability
  {
    public:
    // value
    // 
    typedef ::xml_schema::Double ValueType;
    typedef ::xsd::cxx::tree::traits< ValueType, char, ::xsd::cxx::tree::schema_type::double_ > ValueTraits;

    const ValueType&
    value () const;

    ValueType&
    value ();

    void
    value (const ValueType& x);

    // Constructors.
    //
    FailureRate (const ValueType&);

    FailureRate (const ::xercesc::DOMElement& e,
                 ::xml_schema::Flags f = 0,
                 ::xml_schema::Container* c = 0);

    FailureRate (const FailureRate& x,
                 ::xml_schema::Flags f = 0,
                 ::xml_schema::Container* c = 0);

    virtual FailureRate*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~FailureRate ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< ValueType > value_;
  };

  class Gate_base: public ::faulttree::ChildNode
  {
    public:
    // Constructors.
    //
    Gate_base (const IdType&);

    Gate_base (const ::xercesc::DOMElement& e,
               ::xml_schema::Flags f = 0,
               ::xml_schema::Container* c = 0);

    Gate_base (const Gate_base& x,
               ::xml_schema::Flags f = 0,
               ::xml_schema::Container* c = 0);

    virtual Gate_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~Gate_base ();
  };

  class And_base: public ::faulttree::Gate
  {
    public:
    // Constructors.
    //
    And_base (const IdType&);

    And_base (const ::xercesc::DOMElement& e,
              ::xml_schema::Flags f = 0,
              ::xml_schema::Container* c = 0);

    And_base (const And_base& x,
              ::xml_schema::Flags f = 0,
              ::xml_schema::Container* c = 0);

    virtual And_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~And_base ();
  };

  class Or_base: public ::faulttree::Gate
  {
    public:
    // Constructors.
    //
    Or_base (const IdType&);

    Or_base (const ::xercesc::DOMElement& e,
             ::xml_schema::Flags f = 0,
             ::xml_schema::Container* c = 0);

    Or_base (const Or_base& x,
             ::xml_schema::Flags f = 0,
             ::xml_schema::Container* c = 0);

    virtual Or_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~Or_base ();
  };

  class Xor_base: public ::faulttree::Gate
  {
    public:
    // Constructors.
    //
    Xor_base (const IdType&);

    Xor_base (const ::xercesc::DOMElement& e,
              ::xml_schema::Flags f = 0,
              ::xml_schema::Container* c = 0);

    Xor_base (const Xor_base& x,
              ::xml_schema::Flags f = 0,
              ::xml_schema::Container* c = 0);

    virtual Xor_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~Xor_base ();
  };

  class VotingOr_base: public ::faulttree::Gate
  {
    public:
    // k
    // 
    typedef ::xml_schema::Int KType;
    typedef ::xsd::cxx::tree::traits< KType, char > KTraits;

    const KType&
    k () const;

    KType&
    k ();

    void
    k (const KType& x);

    // Constructors.
    //
    VotingOr_base (const IdType&,
                   const KType&);

    VotingOr_base (const ::xercesc::DOMElement& e,
                   ::xml_schema::Flags f = 0,
                   ::xml_schema::Container* c = 0);

    VotingOr_base (const VotingOr_base& x,
                   ::xml_schema::Flags f = 0,
                   ::xml_schema::Container* c = 0);

    virtual VotingOr_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~VotingOr_base ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< KType > k_;
  };

  class DynamicGate_base: public ::faulttree::Gate
  {
    public:
    // Constructors.
    //
    DynamicGate_base (const IdType&);

    DynamicGate_base (const ::xercesc::DOMElement& e,
                      ::xml_schema::Flags f = 0,
                      ::xml_schema::Container* c = 0);

    DynamicGate_base (const DynamicGate_base& x,
                      ::xml_schema::Flags f = 0,
                      ::xml_schema::Container* c = 0);

    virtual DynamicGate_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~DynamicGate_base ();
  };

  class Idlist: public ::xml_schema::SimpleType,
    public ::xsd::cxx::tree::list< ::xml_schema::String, char >
  {
    public:
    Idlist ();

    Idlist (size_type n, const ::xml_schema::String& x);

    template < typename I >
    Idlist (const I& begin, const I& end)
    : ::xsd::cxx::tree::list< ::xml_schema::String, char > (begin, end, this)
    {
    }

    Idlist (const ::xercesc::DOMElement& e,
            ::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0);

    Idlist (const ::xercesc::DOMAttr& a,
            ::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0);

    Idlist (const ::std::string& s,
            const ::xercesc::DOMElement* e,
            ::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0);

    Idlist (const Idlist& x,
            ::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0);

    virtual Idlist*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~Idlist ();
  };

  class Spare_base: public ::faulttree::DynamicGate
  {
    public:
    // primaryID
    // 
    typedef ::xml_schema::String PrimaryIDType;
    typedef ::xsd::cxx::tree::traits< PrimaryIDType, char > PrimaryIDTraits;

    const PrimaryIDType&
    primaryID () const;

    PrimaryIDType&
    primaryID ();

    void
    primaryID (const PrimaryIDType& x);

    void
    primaryID (::std::auto_ptr< PrimaryIDType > p);

    // dormancyFactor
    // 
    typedef ::xml_schema::Double DormancyFactorType;
    typedef ::xsd::cxx::tree::traits< DormancyFactorType, char, ::xsd::cxx::tree::schema_type::double_ > DormancyFactorTraits;

    const DormancyFactorType&
    dormancyFactor () const;

    DormancyFactorType&
    dormancyFactor ();

    void
    dormancyFactor (const DormancyFactorType& x);

    // Constructors.
    //
    Spare_base (const IdType&,
                const PrimaryIDType&,
                const DormancyFactorType&);

    Spare_base (const ::xercesc::DOMElement& e,
                ::xml_schema::Flags f = 0,
                ::xml_schema::Container* c = 0);

    Spare_base (const Spare_base& x,
                ::xml_schema::Flags f = 0,
                ::xml_schema::Container* c = 0);

    virtual Spare_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~Spare_base ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< PrimaryIDType > primaryID_;
    ::xsd::cxx::tree::one< DormancyFactorType > dormancyFactor_;
  };

  class PriorityAnd_base: public ::faulttree::DynamicGate
  {
    public:
    // eventSequence
    // 
    typedef ::faulttree::Idlist EventSequenceType;
    typedef ::xsd::cxx::tree::traits< EventSequenceType, char > EventSequenceTraits;

    const EventSequenceType&
    eventSequence () const;

    EventSequenceType&
    eventSequence ();

    void
    eventSequence (const EventSequenceType& x);

    void
    eventSequence (::std::auto_ptr< EventSequenceType > p);

    // Constructors.
    //
    PriorityAnd_base (const IdType&,
                      const EventSequenceType&);

    PriorityAnd_base (const ::xercesc::DOMElement& e,
                      ::xml_schema::Flags f = 0,
                      ::xml_schema::Container* c = 0);

    PriorityAnd_base (const PriorityAnd_base& x,
                      ::xml_schema::Flags f = 0,
                      ::xml_schema::Container* c = 0);

    virtual PriorityAnd_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~PriorityAnd_base ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< EventSequenceType > eventSequence_;
  };

  class Sequence_base: public ::faulttree::DynamicGate
  {
    public:
    // eventSequence
    // 
    typedef ::faulttree::Idlist EventSequenceType;
    typedef ::xsd::cxx::tree::traits< EventSequenceType, char > EventSequenceTraits;

    const EventSequenceType&
    eventSequence () const;

    EventSequenceType&
    eventSequence ();

    void
    eventSequence (const EventSequenceType& x);

    void
    eventSequence (::std::auto_ptr< EventSequenceType > p);

    // Constructors.
    //
    Sequence_base (const IdType&,
                   const EventSequenceType&);

    Sequence_base (const ::xercesc::DOMElement& e,
                   ::xml_schema::Flags f = 0,
                   ::xml_schema::Container* c = 0);

    Sequence_base (const Sequence_base& x,
                   ::xml_schema::Flags f = 0,
                   ::xml_schema::Container* c = 0);

    virtual Sequence_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~Sequence_base ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< EventSequenceType > eventSequence_;
  };

  class FDEP_base: public ::faulttree::DynamicGate
  {
    public:
    // trigger
    // 
    typedef ::xml_schema::String TriggerType;
    typedef ::xsd::cxx::tree::traits< TriggerType, char > TriggerTraits;

    const TriggerType&
    trigger () const;

    TriggerType&
    trigger ();

    void
    trigger (const TriggerType& x);

    void
    trigger (::std::auto_ptr< TriggerType > p);

    // triggeredEvents
    // 
    typedef ::faulttree::Idlist TriggeredEventsType;
    typedef ::xsd::cxx::tree::traits< TriggeredEventsType, char > TriggeredEventsTraits;

    const TriggeredEventsType&
    triggeredEvents () const;

    TriggeredEventsType&
    triggeredEvents ();

    void
    triggeredEvents (const TriggeredEventsType& x);

    void
    triggeredEvents (::std::auto_ptr< TriggeredEventsType > p);

    // Constructors.
    //
    FDEP_base (const IdType&,
               const TriggerType&,
               const TriggeredEventsType&);

    FDEP_base (const ::xercesc::DOMElement& e,
               ::xml_schema::Flags f = 0,
               ::xml_schema::Container* c = 0);

    FDEP_base (const FDEP_base& x,
               ::xml_schema::Flags f = 0,
               ::xml_schema::Container* c = 0);

    virtual FDEP_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~FDEP_base ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< TriggerType > trigger_;
    ::xsd::cxx::tree::one< TriggeredEventsType > triggeredEvents_;
  };

  class TransferIn: public ::faulttree::ChildNode
  {
    public:
    // fromModelId
    // 
    typedef ::xml_schema::Int FromModelIdType;
    typedef ::xsd::cxx::tree::traits< FromModelIdType, char > FromModelIdTraits;

    const FromModelIdType&
    fromModelId () const;

    FromModelIdType&
    fromModelId ();

    void
    fromModelId (const FromModelIdType& x);

    // maxCosts
    // 
    typedef ::xml_schema::Int MaxCostsType;
    typedef ::xsd::cxx::tree::traits< MaxCostsType, char > MaxCostsTraits;

    const MaxCostsType&
    maxCosts () const;

    MaxCostsType&
    maxCosts ();

    void
    maxCosts (const MaxCostsType& x);

    static MaxCostsType
    maxCostsDefaultValue ();

    // Constructors.
    //
    TransferIn (const IdType&,
                const FromModelIdType&);

    TransferIn (const ::xercesc::DOMElement& e,
                ::xml_schema::Flags f = 0,
                ::xml_schema::Container* c = 0);

    TransferIn (const TransferIn& x,
                ::xml_schema::Flags f = 0,
                ::xml_schema::Container* c = 0);

    virtual TransferIn*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~TransferIn ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< FromModelIdType > fromModelId_;
    ::xsd::cxx::tree::one< MaxCostsType > maxCosts_;
  };

  class UndevelopedEvent_base: public ::faulttree::ChildNode
  {
    public:
    // Constructors.
    //
    UndevelopedEvent_base (const IdType&);

    UndevelopedEvent_base (const ::xercesc::DOMElement& e,
                           ::xml_schema::Flags f = 0,
                           ::xml_schema::Container* c = 0);

    UndevelopedEvent_base (const UndevelopedEvent_base& x,
                           ::xml_schema::Flags f = 0,
                           ::xml_schema::Container* c = 0);

    virtual UndevelopedEvent_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~UndevelopedEvent_base ();
  };

  class BasicEvent_base: public ::faulttree::ChildNode
  {
    public:
    // probability
    // 
    typedef ::faulttree::Probability ProbabilityType;
    typedef ::xsd::cxx::tree::traits< ProbabilityType, char > ProbabilityTraits;

    const ProbabilityType&
    probability () const;

    ProbabilityType&
    probability ();

    void
    probability (const ProbabilityType& x);

    void
    probability (::std::auto_ptr< ProbabilityType > p);

    // Constructors.
    //
    BasicEvent_base (const IdType&,
                     const ProbabilityType&);

    BasicEvent_base (const IdType&,
                     ::std::auto_ptr< ProbabilityType >&);

    BasicEvent_base (const ::xercesc::DOMElement& e,
                     ::xml_schema::Flags f = 0,
                     ::xml_schema::Container* c = 0);

    BasicEvent_base (const BasicEvent_base& x,
                     ::xml_schema::Flags f = 0,
                     ::xml_schema::Container* c = 0);

    virtual BasicEvent_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~BasicEvent_base ();

    // Implementation.
    //
    protected:
    void
    parse (::xsd::cxx::xml::dom::parser< char >&,
           ::xml_schema::Flags);

    protected:
    ::xsd::cxx::tree::one< ProbabilityType > probability_;
  };

  class HouseEvent_base: public ::faulttree::BasicEvent
  {
    public:
    // Constructors.
    //
    HouseEvent_base (const IdType&,
                     const ProbabilityType&);

    HouseEvent_base (const IdType&,
                     ::std::auto_ptr< ProbabilityType >&);

    HouseEvent_base (const ::xercesc::DOMElement& e,
                     ::xml_schema::Flags f = 0,
                     ::xml_schema::Container* c = 0);

    HouseEvent_base (const HouseEvent_base& x,
                     ::xml_schema::Flags f = 0,
                     ::xml_schema::Container* c = 0);

    virtual HouseEvent_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~HouseEvent_base ();
  };

  class IntermediateEvent_base: public ::faulttree::ChildNode
  {
    public:
    // Constructors.
    //
    IntermediateEvent_base (const IdType&);

    IntermediateEvent_base (const ::xercesc::DOMElement& e,
                            ::xml_schema::Flags f = 0,
                            ::xml_schema::Container* c = 0);

    IntermediateEvent_base (const IntermediateEvent_base& x,
                            ::xml_schema::Flags f = 0,
                            ::xml_schema::Container* c = 0);

    virtual IntermediateEvent_base*
    _clone (::xml_schema::Flags f = 0,
            ::xml_schema::Container* c = 0) const;

    virtual 
    ~IntermediateEvent_base ();
  };
}

#include <iosfwd>

#include <xercesc/sax/InputSource.hpp>
#include <xercesc/dom/DOMDocument.hpp>
#include <xercesc/dom/DOMErrorHandler.hpp>

namespace faulttree
{
  // Parse a URI or a local file.
  //

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (const ::std::string& uri,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (const ::std::string& uri,
             ::xml_schema::ErrorHandler& eh,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (const ::std::string& uri,
             ::xercesc::DOMErrorHandler& eh,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  // Parse std::istream.
  //

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (::std::istream& is,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (::std::istream& is,
             ::xml_schema::ErrorHandler& eh,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (::std::istream& is,
             ::xercesc::DOMErrorHandler& eh,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (::std::istream& is,
             const ::std::string& id,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (::std::istream& is,
             const ::std::string& id,
             ::xml_schema::ErrorHandler& eh,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (::std::istream& is,
             const ::std::string& id,
             ::xercesc::DOMErrorHandler& eh,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  // Parse xercesc::InputSource.
  //

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (::xercesc::InputSource& is,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (::xercesc::InputSource& is,
             ::xml_schema::ErrorHandler& eh,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (::xercesc::InputSource& is,
             ::xercesc::DOMErrorHandler& eh,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  // Parse xercesc::DOMDocument.
  //

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (const ::xercesc::DOMDocument& d,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());

  ::std::auto_ptr< ::faulttree::FaultTree >
  faultTree (::xml_schema::dom::auto_ptr< ::xercesc::DOMDocument >& d,
             ::xml_schema::Flags f = 0,
             const ::xml_schema::Properties& p = ::xml_schema::Properties ());
}

#include <iosfwd>

#include <xercesc/dom/DOMDocument.hpp>
#include <xercesc/dom/DOMErrorHandler.hpp>
#include <xercesc/framework/XMLFormatter.hpp>

#include <xsd/cxx/xml/dom/auto-ptr.hxx>

namespace faulttree
{
  void
  operator<< (::xercesc::DOMElement&, const Annotation&);

  void
  operator<< (::xercesc::DOMAttr&, const Annotation&);

  void
  operator<< (::xml_schema::ListStream&,
              const Annotation&);

  void
  operator<< (::xercesc::DOMElement&, const Probability&);

  void
  operator<< (::xercesc::DOMAttr&, const Probability&);

  void
  operator<< (::xml_schema::ListStream&,
              const Probability&);

  void
  operator<< (::xercesc::DOMElement&, const AnnotatedElement&);

  void
  operator<< (::xercesc::DOMElement&, const Model&);

  void
  operator<< (::xercesc::DOMElement&, const Node_base&);

  void
  operator<< (::xercesc::DOMElement&, const ChildNode_base&);

  void
  operator<< (::xercesc::DOMElement&, const FaultTree&);

  // Serialize to std::ostream.
  //

  void
  faultTree (::std::ostream& os,
             const ::faulttree::FaultTree& x, 
             const ::xml_schema::NamespaceInfomap& m = ::xml_schema::NamespaceInfomap (),
             const ::std::string& e = "UTF-8",
             ::xml_schema::Flags f = 0);

  void
  faultTree (::std::ostream& os,
             const ::faulttree::FaultTree& x, 
             ::xml_schema::ErrorHandler& eh,
             const ::xml_schema::NamespaceInfomap& m = ::xml_schema::NamespaceInfomap (),
             const ::std::string& e = "UTF-8",
             ::xml_schema::Flags f = 0);

  void
  faultTree (::std::ostream& os,
             const ::faulttree::FaultTree& x, 
             ::xercesc::DOMErrorHandler& eh,
             const ::xml_schema::NamespaceInfomap& m = ::xml_schema::NamespaceInfomap (),
             const ::std::string& e = "UTF-8",
             ::xml_schema::Flags f = 0);

  // Serialize to xercesc::XMLFormatTarget.
  //

  void
  faultTree (::xercesc::XMLFormatTarget& ft,
             const ::faulttree::FaultTree& x, 
             const ::xml_schema::NamespaceInfomap& m = ::xml_schema::NamespaceInfomap (),
             const ::std::string& e = "UTF-8",
             ::xml_schema::Flags f = 0);

  void
  faultTree (::xercesc::XMLFormatTarget& ft,
             const ::faulttree::FaultTree& x, 
             ::xml_schema::ErrorHandler& eh,
             const ::xml_schema::NamespaceInfomap& m = ::xml_schema::NamespaceInfomap (),
             const ::std::string& e = "UTF-8",
             ::xml_schema::Flags f = 0);

  void
  faultTree (::xercesc::XMLFormatTarget& ft,
             const ::faulttree::FaultTree& x, 
             ::xercesc::DOMErrorHandler& eh,
             const ::xml_schema::NamespaceInfomap& m = ::xml_schema::NamespaceInfomap (),
             const ::std::string& e = "UTF-8",
             ::xml_schema::Flags f = 0);

  // Serialize to an existing xercesc::DOMDocument.
  //

  void
  faultTree (::xercesc::DOMDocument& d,
             const ::faulttree::FaultTree& x,
             ::xml_schema::Flags f = 0);

  // Serialize to a new xercesc::DOMDocument.
  //

  ::xml_schema::dom::auto_ptr< ::xercesc::DOMDocument >
  faultTree (const ::faulttree::FaultTree& x, 
             const ::xml_schema::NamespaceInfomap& m = ::xml_schema::NamespaceInfomap (),
             ::xml_schema::Flags f = 0);

  void
  operator<< (::xercesc::DOMElement&, const TopEvent_base&);

  void
  operator<< (::xercesc::DOMElement&, const CrispProbability&);

  void
  operator<< (::xercesc::DOMElement&, const FailureRate&);

  void
  operator<< (::xercesc::DOMElement&, const Gate_base&);

  void
  operator<< (::xercesc::DOMElement&, const And_base&);

  void
  operator<< (::xercesc::DOMElement&, const Or_base&);

  void
  operator<< (::xercesc::DOMElement&, const Xor_base&);

  void
  operator<< (::xercesc::DOMElement&, const VotingOr_base&);

  void
  operator<< (::xercesc::DOMElement&, const DynamicGate_base&);

  void
  operator<< (::xercesc::DOMElement&, const Idlist&);

  void
  operator<< (::xercesc::DOMAttr&, const Idlist&);

  void
  operator<< (::xml_schema::ListStream&,
              const Idlist&);

  void
  operator<< (::xercesc::DOMElement&, const Spare_base&);

  void
  operator<< (::xercesc::DOMElement&, const PriorityAnd_base&);

  void
  operator<< (::xercesc::DOMElement&, const Sequence_base&);

  void
  operator<< (::xercesc::DOMElement&, const FDEP_base&);

  void
  operator<< (::xercesc::DOMElement&, const TransferIn&);

  void
  operator<< (::xercesc::DOMElement&, const UndevelopedEvent_base&);

  void
  operator<< (::xercesc::DOMElement&, const BasicEvent_base&);

  void
  operator<< (::xercesc::DOMElement&, const HouseEvent_base&);

  void
  operator<< (::xercesc::DOMElement&, const IntermediateEvent_base&);
}

#include <xsd/cxx/post.hxx>

// Begin epilogue.
//
#include "Visitor.h"
//
// End epilogue.

#endif // C__DEV_FUZZTREES_FUZZTREECONFIGURATION_XML_FAULTTREE_H
