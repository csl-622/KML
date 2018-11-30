import ArticleLengthVsRevision
import NumberOfExternalLinksVSRevision
import NumberOfImagesVSRevision
import NumberOfNounsVSRevision
import NumberOfReferencesVSRevision
import NumberOfSectionsVSRevision

path_of_XML = "/home/paras/KML/resources/Indian Institute of Technology Ropar.xml"
path_of_KML = "/home/paras/KML/compressed-KML/compressedIIT.kml"

print("Please Wait...")
ArticleLengthVsRevision.main(path_of_XML, path_of_KML)
print("1/6 complete")
NumberOfExternalLinksVSRevision.main(path_of_XML, path_of_KML)
print("2/6 complete")
NumberOfImagesVSRevision.main(path_of_XML, path_of_KML)
print("3/6 complete")
NumberOfReferencesVSRevision.main(path_of_XML, path_of_KML)
print("4/6 complete")
NumberOfSectionsVSRevision.main(path_of_XML, path_of_KML)
print("5/6 complete")
NumberOfNounsVSRevision.main(path_of_XML, path_of_KML)
print("6/6 complete")