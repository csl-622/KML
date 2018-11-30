import ArticleLengthVsRevision
import NumberOfExternalLinksVSRevision
import NumberOfImagesVSRevision
import NumberOfNounsVSRevision
import NumberOfReferencesVSRevision
import NumberOfSectionsVSRevision
import matplotlib.pyplot as plt


path_of_XML = "/home/paras/KML/resources/Indian Institute of Technology Ropar.xml"
path_of_KML = "/home/paras/KML/compressed-KML/compressedIIT.kml"
x = []
y1 = []
y2 = []

print("Please Wait...")
result = ArticleLengthVsRevision.main(path_of_XML, path_of_KML)
x.append("Length")
y1.append(result[1]-result[0])
y2.append(result[2]-result[1])

print("1/6 complete")
result = NumberOfExternalLinksVSRevision.main(path_of_XML, path_of_KML)
x.append("Links")
y1.append(result[1]-result[0])
y2.append(result[2]-result[1])

print("2/6 complete")
result = NumberOfImagesVSRevision.main(path_of_XML, path_of_KML)
x.append("Images")
y1.append(result[1]-result[0])
y2.append(result[2]-result[1])

print("3/6 complete")
result = NumberOfReferencesVSRevision.main(path_of_XML, path_of_KML)
x.append("References")
y1.append(result[1]-result[0])
y2.append(result[2]-result[1])

print("4/6 complete")
result = NumberOfSectionsVSRevision.main(path_of_XML, path_of_KML)
x.append("Sections")
y1.append(result[1]-result[0])
y2.append(result[2]-result[1])


print("5/6 complete")
result = NumberOfNounsVSRevision.main(path_of_XML, path_of_KML)
x.append("Nouns")
y1.append(result[1]-result[0])
y2.append(result[2]-result[1])

print("6/6 complete")

plt.plot(x, y1, label = "XML") 
plt.plot(x, y2, label = "KML", linestyle='dashed') 
plt.xlabel('Analysis on: ') 
plt.ylabel('Time in seconds') 
plt.title('Time in seconds vs Analysis used') 
plt.savefig('Time_Analysis')    
