from src.algoritmo_burbuja import ordenadorArray
import pytest

def testAlgoritmoBurbuja1():
    assert ordenadorArray([1,4,3,2,5]) == [1,2,3,4,5]
def testAlgoritmoBurbuja2():
    assert ordenadorArray([16,20,80,32,45,59]) == [16,20,32,45,59,80]

if __name__ == "__main__":
    pytest.main()