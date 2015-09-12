from ..parser .constants import *
from ..parser .utils import htmlspecialchars ,tag2class 

from .exception import *

ENABLE_VALIDATION =True 

class XHPyStrictValidator (object ):
  def __init__ (self ):

    self .ii =None 

  def _safe (self ,cast ,val ):
    try :
      return cast (val )
    except (ValueError ,TypeError ):
      raise XHPyInvalidAttributeException (element ,decl [attr ][1 ],attr ,val )

  def validateAttributeValue (self ,element ,attr ,val ):
    if val is None :
      return None 

    that =element 
    decl =that ._xhpyAttributeDeclaration ()
    while attr not in decl :
      if not isinstance (that ,xhpy_x__base ):
        raise XHPyAttributeNotSupportedException (element ,attr )
      that =super (type (that ),that )
      decl =that ._xhpyAttributeDeclaration ()
    attr_type =decl [attr ][0 ]
    if attr_type ==TYPE_STRING :
      return self ._safe (str ,val )
    if attr_type ==TYPE_BOOL :
      return self ._safe (bool ,val )
    if attr_type ==TYPE_INT :
      return self ._safe (int ,val )
    if attr_type ==TYPE_FLOAT :
      return self ._safe (float ,val )
    if attr_type ==TYPE_LIST :
      return self ._safe (list ,val )
    if attr_type ==TYPE_OBJECT :
      if not isinstance (val ,decl [attr ][1 ]):
        raise XHPyInvalidAttributeException (element ,decl [attr ][1 ],attr ,val )
      return val 
    if attr_type ==TYPE_VAR :
      return val 
    if attr_type ==TYPE_ENUM :
      for enum in decl [attr ][1 ]:
        if enum ==val :
          return val 
      enums ='enum("'+'","'.join (decl [attr ][1 ])+'")'
      raise XHPyInvalidAttributeException (element ,enums ,attr ,val )

  def validateChildren (self ,element ):
    decl =element ._xhpyChildrenDeclaration ()
    if decl ==CHILD_DECL_ANY :

      return 
    if decl ==CHILD_DECL_EMPTY :

      if element ._children :
        raise XHPyInvalidChildrenException (element ,0 )
      return 
    self .ii =0 
    if not self .validateChildrenExpression (element ,decl )or self .ii <len (element ._children ):
      raise XHPyInvalidChildrenException (element ,self .ii )

  def validateChildrenExpression (self ,element ,decl ):
    n =len (element ._children )
    if decl [0 ]==CHILD_ATOM_ANY :

      if self .ii <n :
        self .ii +=1 
        return True 
      return False 
    if decl [0 ]==CHILD_ATOM_PCDATA :

      if self .ii <n and not isinstance (element ._children [self .ii ],xhpy_x__base ):
        self .ii +=1 
        return True 
      return False 
    if decl [0 ]==CHILD_ATOM_SPECIFIC :

      if self .ii <n and isinstance (element ._children [self .ii ],decl [1 ]):
        self .ii +=1 
        return True 
      return False 
    if decl [0 ]==CHILD_ATOM_CATEGORY :

      if self .ii <n and isinstance (element ._children [self .ii ],xhpy_x__base )and element ._children [self .ii ].categoryOf (decl [1 ]):
        self .ii +=1 
        return True 
      return False 
    if decl [0 ]==CHILD_EXPR_ONE :

      return self .validateChildrenExpression (element ,decl [1 ])
    if decl [0 ]==CHILD_EXPR_ZERO_OR_MORE :

      while self .validateChildrenExpression (element ,decl [1 ]):
        pass 
      return True 
    if decl [0 ]==CHILD_EXPR_ZERO_OR_ONE :

      if self .validateChildrenExpression (element ,decl [1 ]):
        pass 
      return True 
    if decl [0 ]==CHILD_EXPR_ONE_OR_MORE :

      if not self .validateChildrenExpression (element ,decl [1 ]):
        return False 
      while self .validateChildrenExpression (element ,decl [1 ]):
        pass 
      return True 
    if decl [0 ]==CHILD_EXPR_CONCAT :

      oindex =self .ii 
      for d in decl [1 ]:
        if not self .validateChildrenExpression (element ,d ):
          self .ii =oindex 
          return False 
      return True 
    if decl [0 ]==CHILD_EXPR_OR :

      for d in decl [1 ]:
        if self .validateChildrenExpression (element ,d ):
          return True 
      return False 

class xhpy_x__base (object ):
  """
  A validator for XHPy attribute and child declarations.
  """
  _validator =XHPyStrictValidator ()

  """
  Defined in elements by the `attribute` keyword. The declaration is simple.
  There is a keyed array, with each key being an attribute. Each value is
  an array with 4 elements. The first is the attribute type. The second is
  meta-data about the attribute. The third is a default value (null for
  none). And the fourth is whether or not this value is required.
  Attribute types are suggested by the TYPE_* constants.
  """
  def _xhpyAttributeDeclaration (self ):
    return {}

  """
  Defined in elements by the `category` keyword. This is just a list of all
  categories an element belongs to. Each category is a key with value 1.
  """
  def _xhpyCategoryDeclaration (self ):
    return []

  """
  Defined in elements by the `children` keyword. This returns a pattern of
  allowed children. The return value is potentially very complicated. The
  two simplest are 0 and 1 which mean no children and any children,
  respectively. Otherwise you're dealing with an array which is just the
  biggest mess you've ever seen.
  """
  def _xhpyChildrenDeclaration (self ):
    return CHILD_DECL_ANY 

  def renderChildrenDeclaration (self ):
    """
    Render the children declaration in readable format. Used in exception
    output.
    """
    decl =self ._xhpyChildrenDeclaration ()
    if decl ==CHILD_DECL_ANY :
      return 'any'
    if decl ==CHILD_DECL_EMPTY :
      return 'empty'
    def _helper (decl ):
      if decl [0 ]==CHILD_ATOM_ANY :
        return 'any'
      if decl [0 ]==CHILD_ATOM_PCDATA :
        return 'pcdata'
      if decl [0 ]==CHILD_ATOM_CATEGORY :
        return decl [1 ]
      if decl [0 ]==CHILD_ATOM_SPECIFIC :
        return decl [1 ].__name__ 
      if decl [0 ]==CHILD_EXPR_ONE :
        return _helper (decl [1 ])
      if decl [0 ]==CHILD_EXPR_ZERO_OR_ONE :
        return "%s?"%_helper (decl [1 ])
      if decl [0 ]==CHILD_EXPR_ZERO_OR_MORE :
        return "%s*"%_helper (decl [1 ])
      if decl [0 ]==CHILD_EXPR_ONE_OR_MORE :
        return "%s+"%_helper (decl [1 ])
      if decl [0 ]==CHILD_EXPR_CONCAT :
        return ','.join ([_helper (d )for d in decl [1 ]])
      if decl [0 ]==CHILD_EXPR_OR :
        return '|'.join ([_helper (d )for d in decl [1 ]])
    return _helper (decl )

  def __init__ (self ):
    raise NotImplementedError ('not implemented!')

  def __unicode__ (self ):
    raise NotImplementedError ('not implemented!')

  def __str__ (self ):
    return unicode (self ).encode ('utf-8')

  def appendChild (self ,child ):
    raise NotImplementedError ('not implemented!')

  def getAttribute (self ,attr ):
    raise NotImplementedError ('not implemented!')

  def setAttribute (self ,attr ,val ):
    raise NotImplementedError ('not implemented!')

  def categoryOf (self ,cat ):
    raise NotImplementedError ('not implemented!')

  @classmethod 
  def renderChild (cls ,child ):
    if isinstance (child ,xhpy_x__base ):
      return unicode (child )
    if isinstance (child ,list ):
      raise XHPyRenderListException ('Can not render list!')
    return htmlspecialchars (unicode (child ))

class xhpy_x__composable_element (xhpy_x__base ):
  def _init (self ):
    pass 

  def __init__ (self ,attributes ={},children =[],source =None ):
    self .source =source 
    if attributes and ENABLE_VALIDATION :
      for key in attributes :
        attributes [key ]=self ._validator .validateAttributeValue (self ,key ,attributes [key ])
    self ._attributes =attributes 
    self ._children =[]
    for child in children :
      self .appendChild (child )

  def appendChild (self ,child ):
    """
    Adds a child to the end of this node. If you give an array to this method
    then it will behave like a DocumentFragment.
    """
    if isinstance (child ,list ):
      for c in child :
        self .appendChild (c )
    elif isinstance (child ,xhpy_x__frag ):
      self ._children +=child ._children 
    elif child is not None :
      self ._children .append (child )
    return self 

  def getChildren (self ,tag_name =None ):
    """
    Fetches all direct children of this element that match a particular tag
    name (or all children if no tag is given)
    """
    if not tag_name :
      return self ._children 
    tag_name =tag2class (tag_name )
    return [child for child in self ._children if child .__class__ .__name__ ==tag_name ]

  def getNumChildren (self ,tag_name =None ):
    return len (self .getChildren (tag_name ))

  def getFirstChild (self ):
    """
    Fetches the first child of this element. If there are no children, an
    exception will be thrown.
    """
    return self ._children [0 ]

  def getAttribute (self ,attr ):
    """
    Fetches an attribute from this elements attribute store. If attr is not
    defined in the store, and default is null an exception will be thrown.
    """
    if attr in self ._attributes :
      return self ._attributes [attr ]
    decl =self ._xhpyAttributeDeclaration ()
    if attr not in decl :
      raise XHPyAttributeNotSupportedException (self ,attr )
    elif decl [attr ][3 ]:
      raise XHPyAttributeRequiredException (self ,attr )
    else :
      return decl [attr ][2 ]

  def getAttributes (self ):
    return self ._attributes 

  def setAttribute (self ,attr ,val ):
    """
    Sets an attribute in this element's attribute store.
    """
    if ENABLE_VALIDATION :
      val =self ._validator .validateAttributeValue (self ,attr ,val )
    self ._attributes [attr ]=val 
    return self 

  def _flushElementChildren (self ):
    ln =len (self ._children )
    for ii in xrange (ln ):
      child =self ._children [ii ]
      if isinstance (child ,xhpy_x__element ):
        while isinstance (child ,xhpy_x__element ):
          if ENABLE_VALIDATION :
            self ._validator .validateChildren (child )
          child =child .render ()
        if not isinstance (child ,xhpy_x__primitive ):
          raise XHPyCoreRenderException (self ._children [ii ],child )
        if isinstance (child ,xhpy_x__frag ):
          self ._children =self ._children [:ii ]+child ._children +self ._children [ii +1 :]
          ln =len (self ._children )
          ii -=1 
        else :
          self ._children [ii ]=child 

  def categoryOf (self ,c ):
    return c in self ._xhpyCategoryDeclaration ()

class xhpy_x__primitive (xhpy_x__composable_element ):
  """
  :x:primitive lays down the foundation for very low-level elements. You
  should directly :x:primitive only if you are creating a core element that
  needs to directly implement stringify(). All other elements should subclass
  from :x:element.
  """

  def stringify (self ):
    pass 

  def __unicode__ (self ):
    self ._flushElementChildren ()
    if ENABLE_VALIDATION :
      self ._validator .validateChildren (self )
    return self .stringify ()

class xhpy_x__element (xhpy_x__composable_element ):
  """
  :x:element defines an interface that all user-land elements should subclass
  from. The main difference between :x:element and :x:primitive is that
  subclasses of :x:element should implement `render()` instead of `stringify`.
  This is important because most elements should not be dealing with strings
  of markup.
  """

  def __unicode__ (self ):
    that =self 
    if ENABLE_VALIDATION :
      self ._validator .validateChildren (that )
      that =that .render ()
      while isinstance (that ,xhpy_x__element ):
        self ._validator .validateChildren (that )
        that =that .render ()
      if not isinstance (that ,xhpy_x__composable_element ):
        raise XHPyCoreRenderException (self ,that )
    else :
      that =that .render ()
      while isinstance (that ,xhpy_x__element ):
        that =that .render ()
    return unicode (that )

class xhpy_x__frag (xhpy_x__primitive ):
  """
  An <x:frag /> is a transparent wrapper around any number of elements. When
  you render it just the children will be rendered. When you append it to an
  element the <x:frag /> will disappear and each child will be sequentially
  appended to the element.
  """
  def stringify (self ):
    buf =''
    for child in self .getChildren ():
      buf +=xhpy_x__base .renderChild (child )
    return buf 
