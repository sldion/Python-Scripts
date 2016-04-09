import collections
import types


#implement the parallization of a dataset
class RDD:
    data = None
    def Map(self, fun, preservesPartioning = False):
        rdd = RDD()
        aMap = [fun(element) for element in self.data]
        rdd.data = aMap
        return rdd

    def collect(self):
        print(type(self.data))
        if isinstance(self.data, dict):
            listdata = list(self.data.items())
            return listdata
        else:
            try:
                listdata = [item for item in self.data]
                return listdata
            except:
                return self.data


    #Reduces the dataset based on fun
    def Reduce(self, fun):
        it = iter(self.data)

        total = next(it)
        for element in self.data[1:]:
            total = fun(total, element)
        return total

    # pass a fucntion to
    # returns a rdd object with tuples of the original and the function
    def keyBy(self, fun):
        aMap = []
        t = RDD()
        aMap = [(fun(element),element) for element in self.data]
        t.data = tuple(aMap)
        return t

    # pass a list of key value pairs counts the keys in the list retrns a dictionary
    # of the results
    def countByKey(self):
        keys = [element[0] for element in self.data]
        my_dict = {x:keys.count(x) for x in keys}
        return my_dict

    def Join(self):

        return data

#creats an RDD object with the data supllied to data
def parallelize(data):
    pdata = RDD()
    pdata.data = data
    return pdata
