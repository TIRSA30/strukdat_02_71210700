import timeit

n = 10 #Misalkan n 10
def fiboiter(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a
x = ("Fibonnacci secara iteratif", fiboiter(n))

def fiborek(n):
    if(n <= 2):
        return 1
    else:
        return(fiborek(n-1)+fiborek(n-2))
y = fiborek(n)


#iteratif
for i in range(1, 100):
    start = timeit.default_timer()
    m = fiboiter(i)
    end = timeit.default_timer()
    waktu = start-end
 
for j in range(1,100):
    start = timeit.default_timer()
    y = fiborek(i)
    end = timeit.default_timer()
    waktu = start-end

    print("n = {}, interaktif {:.10f} detik" .format(i, end-start), "rekrusif {:.10f} detik" .format(j, end-start))
# print('Ukuran', )

