class Underscore(object):
    
    def map(self, arr, lambada):
        m = []
        for el in arr:
            m.append(lambada(arr[el-1]))
        return m
    
    def reduce(self, arr, lambada):
        the_val = 0
        for el in arr:
            the_val = the_val + lambada(arr[el-1])
        return the_val

    def find(self, arr, lambada):
        for el in arr:
            if lambada(arr[el-1]):
                return arr[el-1]

    def filter(self, arr, lambada):
        f = []
        for el in arr:
            if lambada(arr[el-1]):
                f.append(arr[el-1])
        return f

    def reject(self, arr, lambada):
        r = []
        for el in arr:
            if not lambada(arr[el-1]):
                r.append(arr[el-1])
        return r

_ = Underscore()

cute_array = [1,2,3,4,5]

threes = _.map(cute_array, lambda x: 3*x)

sadies_mult = _.reduce(cute_array, lambda x: x * 3)

find = _.find(cute_array, lambda x: x % 2 == 0)

evens = _.filter(cute_array, lambda x: x%2 == 0)

reject = _.reject(cute_array, lambda x: x%2 == 0)
