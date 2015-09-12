"""
Defines existing HTML elements (including some jank deprecated ones!), along
with a series of base classes for supporting common HTML attributes and
operations.
"""

from .core import xhpy_x__base ,xhpy_x__primitive 
from ..parser .utils import get_probably_unique_id ,htmlspecialchars 

class xhpy_xhpy__html_element (xhpy_x__primitive ):
  def _xhpyAttributeDeclaration (self ):return {'accesskey':[1 ,None ,'',False ],'class':[1 ,None ,'',False ],'dir':[1 ,None ,'',False ],'id':[1 ,None ,'',False ],'lang':[1 ,None ,'',False ],'style':[1 ,None ,'',False ],'tabindex':[1 ,None ,'',False ],'title':[1 ,None ,'',False ],'onabort':[1 ,None ,'',False ],'onblur':[1 ,None ,'',False ],'onchange':[1 ,None ,'',False ],'onclick':[1 ,None ,'',False ],'ondblclick':[1 ,None ,'',False ],'onerror':[1 ,None ,'',False ],'onfocus':[1 ,None ,'',False ],'onkeydown':[1 ,None ,'',False ],'onkeypress':[1 ,None ,'',False ],'onkeyup':[1 ,None ,'',False ],'onload':[1 ,None ,'',False ],'onmousedown':[1 ,None ,'',False ],'onmousemove':[1 ,None ,'',False ],'onmouseout':[1 ,None ,'',False ],'onmouseover':[1 ,None ,'',False ],'onmouseup':[1 ,None ,'',False ],'onreset':[1 ,None ,'',False ],'onresize':[1 ,None ,'',False ],'onselect':[1 ,None ,'',False ],'onsubmit':[1 ,None ,'',False ],'onunload':[1 ,None ,'',False ],'onmouseenter':[1 ,None ,'',False ],'onmouseleave':[1 ,None ,'',False ],'selected':[1 ,None ,'',False ],'otherButtonLabel':[1 ,None ,'',False ],'otherButtonHref':[1 ,None ,'',False ],'otherButtonClass':[1 ,None ,'',False ],'type':[1 ,None ,'',False ],'replaceCaret':[1 ,None ,'',False ],'replaceChildren':[1 ,None ,'',False ]}
  def requireUniqueId (self ):
    id =self .getAttribute ('id')
    if not id :
      id =get_probably_unique_id ()
      self .setAttribute ('id',id )
    return id 

  def renderBaseAttrs (self ):
    buf ='<'+self .tagName 
    attributes =self .getAttributes ()
    for key in attributes :
      val =unicode (attributes [key ])
      if val is not None and val is not False :
        buf +=' '+htmlspecialchars (key )+'="'+htmlspecialchars (val ,True )+'"'
    return buf 

  def addClass (self ,klass ):
    klass =klass .strip ()
    currentClasses =self .getAttribute ('class')
    tmp =' '+currentClasses +' '
    has =tmp .find (' '+klass +' ')
    if has !=-1 :
      return self 
    tmp =currentClasses +' '+klass 
    self .setAttribute ('class',tmp .strip ())
    return self 

  def stringify (self ):
    buf =self .renderBaseAttrs ()+'>'
    for child in self .getChildren ():
      buf +=xhpy_x__base .renderChild (child )
    buf +='</'+self .tagName +'>'
    return buf 

class xhpy_xhpy__html_singleton (xhpy_xhpy__html_element ):
  """
  Subclasses of :xhpy:html-singleton may not contain children. When rendered they
  will be in singleton (<img />, <br />) form.
  """
  def _xhpyChildrenDeclaration (self ):return 0 
  def stringify (self ):
    return self .renderBaseAttrs ()+' />'

class xhpy_xhpy__pseudo_singleton (xhpy_xhpy__html_element ):
  """
  Subclasses of :xhpy:pseudo-singleton may contain exactly zero or one
  children. When rendered they will be in full open/close form, no matter how
  many children there are.
  """
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata'))])]))])])
  def escape (self ,txt ):
    return htmlspecialchars (txt )

  def stringify (self ):
    buf =self .renderBaseAttrs ()+'>'
    children =self .getChildren ()
    if children :
      buf +=xhpy_x__base .renderChild (children [0 ])
    return buf +'</'+self .tagName +'>'



class xhpy_a (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'href':[1 ,None ,'',False ],'name':[1 ,None ,'',False ],'rel':[1 ,None ,'',False ],'target':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase','%xhpy_interactive']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='a'


class xhpy_abbr (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='abbr'


class xhpy_acronym (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='acronym'


class xhpy_address (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='address'


class xhpy_area (xhpy_xhpy__html_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'alt':[1 ,None ,'',False ],'coords':[1 ,None ,'',False ],'href':[1 ,None ,'',False ],'nohref':[2 ,None ,False ,False ],'shape':[1 ,None ,'',False ],'target':[1 ,None ,'',False ]}
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='area'


class xhpy_b (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='b'


class xhpy_base (xhpy_xhpy__html_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'href':[1 ,None ,'',False ],'target':[1 ,None ,'',False ]}
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='base'


class xhpy_big (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='big'


class xhpy_blockquote (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'cite':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='blockquote'


class xhpy_body (xhpy_xhpy__html_element ):
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='body'


class xhpy_br (xhpy_xhpy__html_singleton ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='br'


class xhpy_button (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'disabled':[2 ,None ,False ,False ],'name':[1 ,None ,'',False ],'type':[7 ,["submit","button","reset"],None ,False ],'value':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase','%xhpy_interactive']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='button'


class xhpy_caption (xhpy_xhpy__html_element ):

  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='caption'


class xhpy_cite (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='cite'


class xhpy_code (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='code'


class xhpy_col (xhpy_xhpy__html_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'align':[7 ,["left","right","center","justify","char"],None ,False ],'char':[1 ,None ,'',False ],'charoff':[3 ,None ,0 ,False ],'span':[3 ,None ,0 ,False ],'valign':[7 ,["top","middle","bottom","baseline"],None ,False ],'width':[1 ,None ,'',False ]}
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='col'


class xhpy_colgroup (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'align':[7 ,["left","right","center","justify","char"],None ,False ],'char':[1 ,None ,'',False ],'charoff':[3 ,None ,0 ,False ],'span':[3 ,None ,0 ,False ],'valign':[7 ,["top","middle","bottom","baseline"],None ,False ],'width':[1 ,None ,'',False ]}
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_col ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='colgroup'


class xhpy_dd (xhpy_xhpy__html_element ):
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='dd'


class xhpy_del (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'cite':[1 ,None ,'',False ],'datetime':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='del'

class xhpy_div (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='div'


class xhpy_dfn (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='dfn'


class xhpy_dl (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(7 ,(2 ,xhpy_dt ))]),(9 ,[(7 ,(2 ,xhpy_dd ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='dl'


class xhpy_dt (xhpy_xhpy__html_element ):
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='dt'


class xhpy_em (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='em'


class xhpy_fieldset (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(4 ,(8 ,[(9 ,[(6 ,(2 ,xhpy_legend ))]),(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='fieldset'


class xhpy_form (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'action':[1 ,None ,'',False ],'accept':[1 ,None ,'',False ],'accept-charset':[1 ,None ,'',False ],'enctype':[1 ,None ,'',False ],'method':[7 ,["get","post"],None ,False ],'name':[1 ,None ,'',False ],'target':[1 ,None ,'',False ],'ajaxify':[2 ,None ,False ,False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='form'


class xhpy_frame (xhpy_xhpy__html_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'frameborder':[2 ,None ,False ,False ],'longdesc':[1 ,None ,'',False ],'marginheight':[3 ,None ,0 ,False ],'marginwidth':[3 ,None ,0 ,False ],'name':[1 ,None ,'',False ],'noresize':[2 ,None ,False ,False ],'scrolling':[7 ,["yes","no","auto"],None ,False ],'src':[1 ,None ,'',False ]}
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='frame'


class xhpy_frameset (xhpy_xhpy__html_element ):
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_frame )),(4 ,(2 ,xhpy_frameset )),(4 ,(2 ,xhpy_noframes ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='frameset'


class xhpy_h1 (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='h1'


class xhpy_h2 (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='h2'


class xhpy_h3 (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='h3'


class xhpy_h4 (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='h4'


class xhpy_h5 (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='h5'


class xhpy_h6 (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='h6'


class xhpy_head (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'profile':[1 ,None ,'',False ]}
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(4 ,(8 ,[(9 ,[(5 ,(3 ,'%xhpy_metadata'))]),(9 ,[(4 ,(2 ,xhpy_title ))]),(9 ,[(5 ,(3 ,'%xhpy_metadata'))]),(9 ,[(6 ,(2 ,xhpy_base ))]),(9 ,[(5 ,(3 ,'%xhpy_metadata'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='head'


class xhpy_hr (xhpy_xhpy__html_singleton ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='hr'


class xhpy_html (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'xmlns':[1 ,None ,'',False ]}
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(4 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_head ))]),(9 ,[(4 ,(2 ,xhpy_body ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='html'


class xhpy_i (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='i'


class xhpy_iframe (xhpy_xhpy__pseudo_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'frameborder':[7 ,["1","0"],None ,False ],'height':[1 ,None ,'',False ],'longdesc':[1 ,None ,'',False ],'marginheight':[3 ,None ,0 ,False ],'marginwidth':[3 ,None ,0 ,False ],'name':[1 ,None ,'',False ],'scrolling':[7 ,["yes","no","auto"],None ,False ],'src':[1 ,None ,'',False ],'width':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase','%xhpy_interactive']
  def _xhpyChildrenDeclaration (self ):return 0 
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='iframe'


class xhpy_img (xhpy_xhpy__html_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'staticsrc':[1 ,None ,'',False ],'alt':[1 ,None ,'',False ],'src':[1 ,None ,'',False ],'height':[1 ,None ,'',False ],'ismap':[2 ,None ,False ,False ],'longdesc':[1 ,None ,'',False ],'usemap':[1 ,None ,'',False ],'width':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='img'


class xhpy_input (xhpy_xhpy__html_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'autocomplete':[7 ,["on","off"],None ,False ],'placeholder':[1 ,None ,'',False ],'accept':[1 ,None ,'',False ],'align':[7 ,["left","right","top","middle","bottom"],None ,False ],'alt':[1 ,None ,'',False ],'checked':[2 ,None ,False ,False ],'disabled':[2 ,None ,False ,False ],'maxlength':[3 ,None ,0 ,False ],'name':[1 ,None ,'',False ],'readonly':[2 ,None ,False ,False ],'size':[3 ,None ,0 ,False ],'src':[1 ,None ,'',False ],'type':[7 ,["button","checkbox","color","date","datetime","datetime-local","email","file","hidden","image","month","number","password","radio","range","reset","search","submit","tel","text","time","url","week"],None ,False ],'value':[1 ,None ,'',False ],'required':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase','%xhpy_interactive']
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='input'


class xhpy_ins (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'cite':[1 ,None ,'',False ],'datetime':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='ins'


class xhpy_kbd (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='kbd'


class xhpy_label (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'for':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase','%xhpy_interactive']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='label'


class xhpy_legend (xhpy_xhpy__html_element ):
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='legend'


class xhpy_li (xhpy_xhpy__html_element ):
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='li'


class xhpy_link (xhpy_xhpy__html_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'charset':[1 ,None ,'',False ],'href':[1 ,None ,'',False ],'hreflang':[1 ,None ,'',False ],'media':[1 ,None ,'',False ],'rel':[1 ,None ,'',False ],'rev':[1 ,None ,'',False ],'target':[1 ,None ,'',False ],'type':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_metadata']
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='link'


class xhpy_map (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'name':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(4 ,(8 ,[(9 ,[(7 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])])),(7 ,(2 ,xhpy_area ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='map'


class xhpy_meta (xhpy_xhpy__html_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'content':[1 ,None ,'',True ],'http-equiv':[7 ,["content-type","content-style-type","expires","refresh","set-cookie"],None ,False ],'http-equiv':[1 ,None ,'',False ],'name':[1 ,None ,'',False ],'scheme':[1 ,None ,'',False ],'charset':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_metadata']
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='meta'


class xhpy_noframes (xhpy_xhpy__html_element ):
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(4 ,(8 ,[(9 ,[(4 ,(3 ,'%xhpy_html_body'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='noframes'


class xhpy_noscript (xhpy_xhpy__html_element ):

  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='noscript'


class xhpy_object (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'align':[7 ,["left","right","top","bottom"],None ,False ],'archive':[1 ,None ,'',False ],'border':[3 ,None ,0 ,False ],'classid':[1 ,None ,'',False ],'codebase':[1 ,None ,'',False ],'codetype':[1 ,None ,'',False ],'data':[1 ,None ,'',False ],'declare':[2 ,None ,False ,False ],'height':[3 ,None ,0 ,False ],'hspace':[3 ,None ,0 ,False ],'name':[1 ,None ,'',False ],'standby':[1 ,None ,'',False ],'type':[1 ,None ,'',False ],'usemap':[1 ,None ,'',False ],'vspace':[3 ,None ,0 ,False ],'width':[3 ,None ,0 ,False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(4 ,(8 ,[(9 ,[(5 ,(2 ,xhpy_param ))]),(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='object'


class xhpy_ol (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_li ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='ol'


class xhpy_optgroup (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'label':[1 ,None ,'',False ],'disabled':[2 ,None ,False ,False ]}
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_option ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='optgroup'


class xhpy_option (xhpy_xhpy__pseudo_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'disabled':[2 ,None ,False ,False ],'label':[1 ,None ,'',False ],'selected':[2 ,None ,False ,False ],'value':[1 ,None ,'',False ]}
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='option'


class xhpy_p (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='p'


class xhpy_param (xhpy_xhpy__pseudo_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'name':[1 ,None ,'',False ],'type':[1 ,None ,'',False ],'value':[1 ,None ,'',False ],'valuetype':[7 ,["data","ref","object"],None ,False ]}
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='param'


class xhpy_pre (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='pre'


class xhpy_q (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'cite':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='q'



class xhpy_s (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='s'


class xhpy_samp (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='samp'


class xhpy_script (xhpy_xhpy__pseudo_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'charset':[1 ,None ,'',False ],'defer':[2 ,None ,False ,False ],'src':[1 ,None ,'',False ],'type':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase','%xhpy_metadata']
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='script'


class xhpy_select (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'disabled':[2 ,None ,False ,False ],'multiple':[2 ,None ,False ,False ],'name':[1 ,None ,'',False ],'size':[3 ,None ,0 ,False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase','%xhpy_interactive']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_option )),(4 ,(2 ,xhpy_optgroup ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='select'


class xhpy_small (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='small'


class xhpy_span (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='span'


class xhpy_strong (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='strong'


class xhpy_style (xhpy_xhpy__pseudo_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'media':[7 ,["screen","tty","tv","projection","handheld","print","braille","aural","all"],None ,False ],'type':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_metadata']
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='style'


class xhpy_sub (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(4 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='sub'


class xhpy_sup (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(4 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='sup'


class xhpy_table (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'border':[3 ,None ,0 ,False ],'cellpadding':[3 ,None ,0 ,False ],'cellspacing':[3 ,None ,0 ,False ],'frame':[7 ,["void","above","below","hsides","lhs","rhs","vsides","box","border"],None ,False ],'rules':[7 ,["none","groups","rows","cols","all"],None ,False ],'summary':[1 ,None ,'',False ],'width':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(4 ,(8 ,[(9 ,[(6 ,(2 ,xhpy_caption ))]),(9 ,[(5 ,(2 ,xhpy_colgroup ))]),(9 ,[(6 ,(2 ,xhpy_thead ))]),(9 ,[(4 ,(8 ,[(9 ,[(4 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_tfoot ))]),(9 ,[(4 ,(8 ,[(9 ,[(7 ,(2 ,xhpy_tbody )),(5 ,(2 ,xhpy_tr ))])]))])])),(4 ,(8 ,[(9 ,[(4 ,(8 ,[(9 ,[(7 ,(2 ,xhpy_tbody )),(5 ,(2 ,xhpy_tr ))])]))]),(9 ,[(6 ,(2 ,xhpy_tfoot ))])]))])]))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='table'


class xhpy_tbody (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'align':[7 ,["right","left","center","justify","char"],None ,False ],'char':[1 ,None ,'',False ],'charoff':[3 ,None ,0 ,False ],'valign':[7 ,["top","middle","bottom","baseline"],None ,False ]}
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_tr ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='tbody'



class xhpy_td (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'abbr':[1 ,None ,'',False ],'align':[7 ,["left","right","center","justify","char"],None ,False ],'axis':[1 ,None ,'',False ],'char':[1 ,None ,'',False ],'charoff':[3 ,None ,0 ,False ],'colspan':[3 ,None ,0 ,False ],'headers':[1 ,None ,'',False ],'rowspan':[3 ,None ,0 ,False ],'scope':[7 ,["col","colgroup","row","rowgroup"],None ,False ],'valign':[7 ,["top","middle","bottom","baseline"],None ,False ]}
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='td'


class xhpy_textarea (xhpy_xhpy__pseudo_singleton ):
  def _xhpyAttributeDeclaration (self ):return {'cols':[3 ,None ,0 ,False ],'rows':[3 ,None ,0 ,False ],'disabled':[2 ,None ,False ,False ],'name':[1 ,None ,'',False ],'readonly':[2 ,None ,False ,False ],'placeholder':[1 ,None ,'',False ],'required':[1 ,None ,'',False ]}
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase','%xhpy_interactive']
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='textarea'


class xhpy_tfoot (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'align':[7 ,["left","right","center","justify","char"],None ,False ],'char':[1 ,None ,'',False ],'charoff':[3 ,None ,0 ,False ],'valign':[7 ,["top","middle","bottom","baseline"],None ,False ]}
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_tr ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='tfoot'


class xhpy_th (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'abbr':[1 ,None ,'',False ],'align':[7 ,["left","right","center","justify","char"],None ,False ],'axis':[1 ,None ,'',False ],'char':[1 ,None ,'',False ],'charoff':[3 ,None ,0 ,False ],'colspan':[3 ,None ,0 ,False ],'rowspan':[3 ,None ,0 ,False ],'scope':[7 ,["col","colgroup","row","rowgroup"],None ,False ],'valign':[7 ,["top","middle","bottom","baseline"],None ,False ]}
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_flow'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='th'


class xhpy_thead (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'align':[7 ,["left","right","center","justify","char"],None ,False ],'char':[1 ,None ,'',False ],'charoff':[3 ,None ,0 ,False ],'valign':[7 ,["top","middle","bottom","baseline"],None ,False ]}
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_tr ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='thead'


class xhpy_title (xhpy_xhpy__pseudo_singleton ):


  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='title'


class xhpy_tr (xhpy_xhpy__html_element ):
  def _xhpyAttributeDeclaration (self ):return {'align':[7 ,["left","right","center","justify","char"],None ,False ],'char':[1 ,None ,'',False ],'charoff':[3 ,None ,0 ,False ],'valign':[7 ,["top","middle","bottom","baseline"],None ,False ]}
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_th )),(4 ,(2 ,xhpy_td ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='tr'


class xhpy_tt (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='tt'



class xhpy_u (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='u'


class xhpy_ul (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_li ))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='ul'


class xhpy_var (xhpy_xhpy__html_element ):
  def _xhpyCategoryDeclaration (self ):return ['%xhpy_flow','%xhpy_phrase']
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(5 ,(8 ,[(9 ,[(4 ,(1 ,'pcdata')),(4 ,(3 ,'%xhpy_phrase'))])]))])])
  def __init__ (self ,attributes ={},children =[]):
    super (xhpy_xhpy__html_element ,self ).__init__ (attributes ,children )
    self .tagName ='var'


class xhpy_x__doctype (xhpy_x__primitive ):
  """
  Render an <html /> element with a DOCTYPE, great for dumping a page to a
  browser. Choose from a wide variety of flavors like XHTML 1.0 Strict, HTML
  4.01 Transitional, and new and improved HTML 5!

  Note: Some flavors may not be available in your area.
  """
  def _xhpyChildrenDeclaration (self ):return (8 ,[(9 ,[(4 ,(8 ,[(9 ,[(4 ,(2 ,xhpy_html ))])]))])])
  def stringify (self ):
    children =self .getChildren ()
    return '<!DOCTYPE html>'+(xhpy_x__base .renderChild (children [0 ]))
