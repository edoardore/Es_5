from Tree import ABR, RB
import random, pickle
from timeit import default_timer as timer
from matplotlib import pyplot as plt


def random_array(n):
    A = range(n)
    for i in range(0, n):
        A[i] = random.randint(0, n * 10)
    return A


def random_array_ordered(n):
    A = range(n)
    return A


def TestInsertRandomABR():
    T = []
    M = []
    dim = 10
    r = 0
    while r < 200:
        j = 0
        while j < 5:
            A = random_array(dim)
            tree = ABR()
            start = timer()
            for i in range(0, dim):
                tree.insert(A[i])
            end = timer()
            time = end - start
            T.append(time)
            j += 1
        sum = 0
        for k in range(0, len(T)):
            sum += T[k]
        media = sum / 10
        M.append(media)
        r += 1
        T[0:len(T)] = []
        dim += 10
    pickle.dump(M, open("m1.p", "wb"))


def TestSearchRandomABR():
    T = []
    M = []
    dim = 10
    r = 0
    while r < 100:
        j = 0
        while j < 5:
            A = random_array(dim)
            tree = ABR()
            for i in range(0, dim):
                tree.insert(A[i])
            start = timer()
            for i in range(0, dim):
                tree.find(A[i])
            end = timer()
            time = end - start
            T.append(time)
            j += 1
        sum = 0
        for k in range(0, len(T)):
            sum += T[k]
        media = sum / 10
        M.append(media)
        r += 1
        T[0:len(T)] = []
        dim += 10
    pickle.dump(M, open("m2.p", "wb"))


def TestSearchOrderedABR():
    T = []
    M = []
    dim = 10
    r = 0
    while r < 75:
        j = 0
        while j < 5:
            A = random_array_ordered(dim)
            tree = ABR()
            for i in range(0, dim):
                tree.insert(A[i])
            start = timer()
            for i in range(0, dim):
                tree.find(A[i])
            end = timer()
            time = end - start
            T.append(time)
            j += 1
        sum = 0
        for k in range(0, len(T)):
            sum += T[k]
        media = sum / 10
        M.append(media)
        r += 1
        T[0:len(T)] = []
        dim += 10
    pickle.dump(M, open("m3.p", "wb"))


def TestDeleteRandomABR():
    T = []
    M = []
    dim = 10
    r = 0
    while r < 200:
        j = 0
        while j < 5:
            A = random_array(dim)
            tree = ABR()
            for i in range(0, dim):
                tree.insert(A[i])
            start = timer()
            for i in range(0, dim):
                tree.delete(A[i])
            end = timer()
            time = end - start
            T.append(time)
            j += 1
        sum = 0
        for k in range(0, len(T)):
            sum += T[k]
        media = sum / 10
        M.append(media)
        r += 1
        T[0:len(T)] = []
        dim += 10
    pickle.dump(M, open("m4.p", "wb"))


def TestDeleteOrderedABR():
    T = []
    M = []
    dim = 10
    r = 0
    while r < 200:
        j = 0
        while j < 5:
            A = random_array_ordered(dim)
            tree = ABR()
            for i in range(0, dim):
                tree.insert(A[i])
            start = timer()
            for i in range(0, dim):
                tree.delete(A[i])
            end = timer()
            time = end - start
            T.append(time)
            j += 1
        sum = 0
        for k in range(0, len(T)):
            sum += T[k]
        media = sum / 10
        M.append(media)
        r += 1
        T[0:len(T)] = []
        dim += 10
    pickle.dump(M, open("m5.p", "wb"))


def TestInsertOrderedABR():
    T = []
    M = []
    dim = 10
    r = 0
    while r < 200:
        j = 0
        while j < 5:
            A = random_array_ordered(dim)
            tree = ABR()
            start = timer()
            for i in range(0, dim):
                tree.insert(A[i])
            end = timer()
            time = end - start
            T.append(time)
            j += 1
        sum = 0
        for k in range(0, len(T)):
            sum += T[k]
        media = sum / 10
        M.append(media)
        r += 1
        T[0:len(T)] = []
        dim += 10
    pickle.dump(M, open("m6.p", "wb"))


def TestInsertRandomRB():
    T = []
    M = []
    dim = 10
    r = 0
    while r < 200:
        j = 0
        while j < 5:
            A = random_array(dim)
            tree = RB()
            start = timer()
            for i in range(0, dim):
                tree.insert(A[i])
            end = timer()
            time = end - start
            T.append(time)
            j += 1
        sum = 0
        for k in range(0, len(T)):
            sum += T[k]
        media = sum / 10
        M.append(media)
        r += 1
        T[0:len(T)] = []
        dim += 10
    pickle.dump(M, open("m7.p", "wb"))


def TestInsertOrderedRB():
    T = []
    M = []
    dim = 10
    r = 0
    while r < 200:
        j = 0
        while j < 5:
            A = random_array_ordered(dim)
            tree = RB()
            start = timer()
            for i in range(0, dim):
                tree.insert(A[i])
            end = timer()
            time = end - start
            T.append(time)
            j += 1
        sum = 0
        for k in range(0, len(T)):
            sum += T[k]
        media = sum / 10
        M.append(media)
        r += 1
        T[0:len(T)] = []
        dim += 10
    pickle.dump(M, open("m8.p", "wb"))


def TestSearchRandomRB():
    T = []
    M = []
    dim = 10
    r = 0
    while r < 100:
        j = 0
        while j < 5:
            A = random_array(dim)
            tree = RB()
            for i in range(0, dim):
                tree.insert(A[i])
            start = timer()
            for i in range(0, dim):
                tree.find(A[i])
            end = timer()
            time = end - start
            T.append(time)
            j += 1
        sum = 0
        for k in range(0, len(T)):
            sum += T[k]
        media = sum / 10
        M.append(media)
        r += 1
        T[0:len(T)] = []
        dim += 10
    pickle.dump(M, open("m9.p", "wb"))


def TestSearchOrderedRB():
    T = []
    M = []
    dim = 10
    r = 0
    while r < 100:
        j = 0
        while j < 5:
            A = random_array_ordered(dim)
            tree = RB()
            for i in range(0, dim):
                tree.insert(A[i])
            start = timer()
            for i in range(0, dim):
                tree.find(A[i])
            end = timer()
            time = end - start
            T.append(time)
            j += 1
        sum = 0
        for k in range(0, len(T)):
            sum += T[k]
        media = sum / 10
        M.append(media)
        r += 1
        T[0:len(T)] = []
        dim += 10
    pickle.dump(M, open("m10.p", "wb"))


def RunAllTest():
    TestDeleteOrderedABR()
    TestDeleteRandomABR()
    TestInsertOrderedABR()
    TestInsertRandomABR()
    TestInsertOrderedRB()
    TestInsertRandomRB()
    TestSearchOrderedABR()
    TestSearchRandomABR()
    TestSearchOrderedRB()
    TestSearchRandomRB()


def PlotTest():
    RunAllTest()
    A = pickle.load(open("m1.p", "rb"))
    B = pickle.load(open("m7.p", "rb"))
    C = pickle.load(open("m6.p", "rb"))
    D = pickle.load(open("m8.p", "rb"))
    E = pickle.load(open("m2.p", "rb"))
    F = pickle.load(open("m3.p", "rb"))
    G = pickle.load(open("m9.p", "rb"))
    H = pickle.load(open("m10.p", "rb"))
    I = pickle.load(open("m4.p", "rb"))
    L = pickle.load(open("m5.p", "rb"))
    plt.plot(A, label="ABR")
    plt.plot(B, label="RB")
    plt.plot(C, label="ABR: elementi ordinati")
    plt.plot(D, label="RB: elementi ordinati")
    plt.legend()
    plt.xlabel("Numero elementi")
    plt.ylabel("Tempo di esecuzione")
    plt.show()
    plt.plot(E, label="ABR: ricerca")
    plt.plot(F, label="ABR: ricerca ordinata")
    plt.plot(G, label="RB: ricerca")
    plt.plot(H, label="RB: ricerca ordinata")
    plt.legend()
    plt.xlabel("Numero elementi")
    plt.ylabel("Tempo di esecuzione")
    plt.show()
    plt.plot(I, label="ABR delete elementi casuali")
    plt.plot(L, label="ABR delete elementi ordinati")
    plt.legend()
    plt.xlabel("Numero elementi")
    plt.ylabel("Tempo di esecuzione")
    plt.show()


PlotTest()
