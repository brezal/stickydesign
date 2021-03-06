from . import energetics_daoe
from . import energetics
from .stickydesign import endarray
import numpy as np

class test_energetics_daoe():
    def setup(self):
        r5dt = endarray(np.random.randint(low=0,high=4,size=(100,7)),'DT')
        r5td = endarray(np.random.randint(low=0,high=4,size=(100,7)),'TD')
        r10dt = endarray(np.random.randint(low=0,high=4,size=(100,12)),'DT')
        r10td = endarray(np.random.randint(low=0,high=4,size=(100,12)),'TD')
        self.sets = [r5dt,r5td,r10dt,r10td]
        self.en = energetics_daoe.energetics_daoe()

    def test_matching_energies_match(self):
        for s in self.sets:
            r1 = self.en.matching_uniform(s)
            r2 = self.en.uniform_loopmismatch(s.ends,s.comps)
            r3 = self.en.uniform_danglemismatch(s.ends,s.comps)
            print(repr(s))
            np.testing.assert_array_almost_equal(r1,r2)
    
    def test_matching_energies_match_combined(self):
        for s in self.sets:
            r1 = self.en.matching_uniform(s)
            r2 = self.en.uniform_combinedmismatch(s.ends,s.comps)
            print(repr(s))
            np.testing.assert_array_almost_equal(r1,r2)

class test_energetics():
    def setup(self):
        r5dt = endarray(np.random.randint(low=0,high=4,size=(100,7)),'DT')
        r5td = endarray(np.random.randint(low=0,high=4,size=(100,7)),'TD')
        r10dt = endarray(np.random.randint(low=0,high=4,size=(100,12)),'DT')
        r10td = endarray(np.random.randint(low=0,high=4,size=(100,12)),'TD')
        self.sets = [r5dt,r5td,r10dt,r10td]
        self.en = energetics.energetics_santalucia()

    def test_matching_energies_match(self):
        for s in self.sets:
            r1 = self.en.matching_uniform(s)
            r2 = self.en.uniform_loopmismatch(s.ends,s.comps)
            r3 = self.en.uniform_danglemismatch(s.ends,s.comps)
            print(repr(s))
            np.testing.assert_array_almost_equal(r1,r2)
            np.testing.assert_array_almost_equal(r1,r3)
