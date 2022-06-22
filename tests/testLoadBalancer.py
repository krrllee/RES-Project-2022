from ast import Load
import sys
sys.path.append('./')
import unittest
from LoadBalancer import LoadBalancer
import socket
from unittest.mock import Mock

class TestLoadBalancer(unittest.TestCase):
    def testNapraviSocket(self):
        lb = LoadBalancer()
        self.assertRaises(TypeError,lb.napraviSocket,"rgsfe")
        self.assertRaises(TypeError,lb.napraviSocket,6)
        self.assertRaises(TypeError,lb.napraviSocket,True)

    def testClientListening(self):
        lb = LoadBalancer()
        self.assertRaises(TypeError,lb.clientListening,True)
        self.assertRaises(TypeError,lb.clientListening,2)

    def testWorkerListening(self):
        lb = LoadBalancer()
        self.assertRaises(TypeError,lb.workerListening,True)
        self.assertRaises(TypeError,lb.workerListening,1)

    def testHandle(self):
        lb = LoadBalancer()
        self.assertRaises(TypeError,lb.handle,"asd")
        self.assertRaises(TypeError,lb.handle,5)
        self.assertRaises(TypeError,lb.handle,False)

    def testPrimiPodatke(self):
        lb = LoadBalancer()
        connection = Mock()
        connection._mock_return_value = "asd".encode()
        self.assertAlmostEqual(lb.primiPodatke(connection),"asd".encode())
        connection.called()
        connection._mock_return_value = "poruka".encode()
        self.assertAlmostEqual(lb.primiPodatke(connection),"poruka".encode())

    def testPrimiKomandu(self):
        lb = LoadBalancer()
        self.assertAlmostEqual(lb.primiKomandu("Poslato:1"),"Poslato")
        self.assertAlmostEqual(lb.primiKomandu("UPALI:0"),"Upali")

    def testUzmiParametre(self):
        lb = LoadBalancer()
        self.assertAlmostEqual(lb.uzmiParametre("Poslato:CODE_DIGITAL:123"),"CODE_DIGITAL:123")
        self.assertAlmostEqual(lb.uzmiParametre("1:1:1"),"1:1:1")

    def testSmjestiPodatke(self):
        lb = LoadBalancer()
        self.assertAlmostEqual(lb.smjestiPodatke([1,2,3,1,2,3,1,2,3,1,2,3],"qwer"),False)
        self.assertAlmostEqual(lb.smjestiPodatke([1,2,3,1,1,2,3],"qwer"),True)
        self.assertAlmostEqual(lb.smjestiPodatke([],"qwer"),True)

    def testUgasiKonekciju(self):
        lb = LoadBalancer()
        connection = Mock()
        povezaniKlijenti = [connection]
        self.assertAlmostEqual(lb.ugasiKlijenta(connection,povezaniKlijenti),True)
        connection.called()
        self.assertAlmostEqual(lb.ugasiKlijenta(connection,[]),False)

    def TestPokreniWorkera(self):
        lb = LoadBalancer()
        self.assertAlmostEqual(lb.pokreniWorker("123"),True)

    def testDostupniWorkeri(self):
        lb = LoadBalancer()
        self.assertAlmostEqual(lb.pronadjiWorkera([True,False,True]),0)
        self.assertAlmostEqual(lb.pronadjiWorkera([False,False,False]),-1)
        self.assertAlmostEqual(lb.pronadjiWorkera([False,False,True]),2)
        self.assertAlmostEqual(lb.pronadjiWorkera([]),-1)

    def testUgasiWorker(self):
        lb = LoadBalancer()
        connection = Mock()
        connections = [connection]
        self.assertAlmostEqual(lb.uzmiWorkera(0,connections,[True]),True)
        connection.called()
        self.assertAlmostEqual(lb.ugasiWorker(0,connections,[]),False)
        self.assertAlmostEqual(lb.ugasiWorker(2,connections,[True]),False)
        self.assertAlmostEqual(lb.ugasiWorker(0,[],[True]),False)

    def testPosaljiWorkeru(self):
        lb = LoadBalancer()
        connection = Mock()
        poruka = "poruka".encode()
        self.assertAlmostEqual(lb.posaljiWorkeru(0,connection,[True],poruka),True)
        connection.called()
        self.assertAlmostEqual(lb.posaljiWorkeru(1,connection,[True],"dgssesda".encode()),False)

    def testWorker(self):
        lb = LoadBalancer()
        self.assertAlmostEqual(lb.uzmiWorkera(1,[True,False]),False)
        self.assertAlmostEqual(lb.uzmiWorkera(2,[4,3,1]),1)
        self.assertAlmostEqual(lb.uzmiWorkera(0,["rdfwsrfs"]),"rdfwsrfs")

    def testDostupnostWorkera(self):
        lb = LoadBalancer()
        self.assertAlmostEqual(lb.provjeriDostupneWorkere([True,False]),False)
        self.assertAlmostEqual(lb.provjeriDostupneWorkere([True]),True)
        self.assertAlmostEqual(lb.provjeriDostupneWorkere([True,True,True,False]),False)
        self.assertAlmostEqual(lb.provjeriDostupneWorkere([True,True]),True)
        self.assertAlmostEqual(lb.provjeriDostupneWorkere([]),True)