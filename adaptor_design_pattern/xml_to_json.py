"""
    Implementation of adaptor design pattern 
    Example : Convert XML to JSON file 
"""

from abc import ABC,abstractmethod

# Adaptee 
class jsonAnalyticsTool:
    def __init__(self):
        self.__json_data = None 

    def setJsonData(self,json_data):
        self.__json_data = json_data 

    def analyzeData(self):
        if self.__json_data:
            file_extention = self.__json_data.split('.')[-1]
            if(file_extention == "json"):
                print(f"[INFO] : file name -> {self.__json_data}")
                print(f"[INFO] : Analyzing JSON file ")
            else:
                raise AssertionError(f"{self.__json_data} this is not json file")
        
        else:
            raise IOError("JSON file is not found")
        

#Interface for adaptor 
class analyticsTools:
    def analyzeData(self):
        raise NotImplementedError("Sub class not implemented")


# Adaptor
class xmlToJsonAdaptor(analyticsTools,jsonAnalyticsTool):

    def __init__(self,xml_data):
        print(f"[INFO] : Converting XML ({xml_data}) file into JSON file")
        self.__json_data = xml_data.split(".")[0] + ".json"
        jsonAnalyticsTool.__init__(self)
        jsonAnalyticsTool.setJsonData(self,self.__json_data)
    
    def analyzeData(self):
        jsonAnalyticsTool.analyzeData(self)

    
def main():
    xml_data = "sample.xml"

    xml_to_json = xmlToJsonAdaptor(xml_data)
    xml_to_json.analyzeData()

if(__name__ == "__main__"):
    main()
