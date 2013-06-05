from nose.tools import *
import unittest

from wicken.dogma import Dogma
from wicken.dogma import MetaReligion
from wicken.dogma import Tenants

from wicken.exceptions import DogmaMetaClassException
from wicken.exceptions import DogmaGetterSetterException
from wicken.exceptions import DogmaDeleteException
class DomgaTest(unittest.TestCase):

    def setUp(self):
        """
        Setup test
        """
        pass    

    
    def tearDown(self):
        """
        Tear down test
        """
        pass
        
        
    def test_init(self):

        
        d = Dogma('CF',{},None)
        assert_equal(d._religion,'CF')
        assert_equal(d._beliefs,{})
        assert_is(d._dataObject,None)
        assert_equal(d.__class__.__name__,'CFDogma')
        
        d = Dogma('CF',{},'foo')
        assert_is(d._dataObject,'foo')
        
        beliefs = {'foo':'bar','bat':'baz'}
        d = Dogma('CF',beliefs,None)
        assert_is(d._beliefs,beliefs)
        assert_is(d.__class__._beliefs, beliefs)
        assert_is(d.__class__._religion, 'CF')
        assert_is_instance(d.__class__.__dict__.get('foo'), Tenants)
        assert_is_instance(d.__class__.__dict__.get('bat'), Tenants)

        bat_tenant = d.__class__.__dict__.get('bat')
        assert_equal(bat_tenant.belief, 'bat')
        assert_equal(bat_tenant.teaching,'baz')
        
        
        with assert_raises_regexp(DogmaMetaClassException,"Blasphemy! The name of your metadata religion"):
            d = Dogma('',{},None)
            
    def test_help(self):    
        pass
        #Can't find a way to test the help?
        
    def test_dogma_set(self):
    
        beliefs = {'foo':'bar','bat':'baz'}
        d = Dogma('CF',beliefs,None)
        with assert_raises_regexp(NotImplementedError,'_set Method is not implemented in the Dogma Base Class!'):
            d._set('foo','bar')
            
        with assert_raises_regexp(DogmaGetterSetterException,"""Error setting the 'foo' property of the class 'CFDogma'"""):
            d.foo = 5
            
        with assert_raises(AttributeError):
            d.not_an_att = 5
        
            
    def test_dogma_delete(self):
    
        beliefs = {'foo':'bar','bat':'baz'}
        d = Dogma('CF',beliefs,None)
        with assert_raises_regexp(NotImplementedError,'_del Method is not implemented in the Dogma Base Class!'):
            d._del('foo')
            
        with assert_raises_regexp(DogmaDeleteException,"""Error deleting the 'foo' property of the class 'CFDogma'"""):
            del d.foo
        
        with assert_raises(AttributeError):
            del d.not_an_att
            
            
    def test_dogma_get(self):
    
        beliefs = {'foo':'bar','bat':'baz'}
        d = Dogma('CF',beliefs,None)
        with assert_raises_regexp(NotImplementedError,'_get Method is not implemented in the Dogma Base Class!'):
            d._get('foo')
            
        with assert_raises_regexp(DogmaGetterSetterException,"""Error getting the 'foo' property of the class 'CFDogma'"""):
            d.foo
            
        with assert_raises(AttributeError):
            d.not_an_att
            
            
    def test_dogma_validate_teaching(self):

        beliefs = {'foo':'bar','bat':'baz'}
        d = Dogma('CF',beliefs,None)
        
        ret = d._validate_teaching('foo','bar')
        assert_is(ret, None)
        
        Dogma._validate_teaching('foo','bar')
        assert_is(ret, None)
        
        
        