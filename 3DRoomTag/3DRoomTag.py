import System

coll_rvtlinks=FilteredElementCollector(doc).OfClass(RevitLinkInstance)
#for n in coll_doc: print n.Name

linkDocs=[]
for link in coll_rvtlinks:
	print link.Name
	linkDocs.append(link.GetLinkDocument())
rooms,roomNames,roomNumbers,roomAreas,roomLocPoints=[],[],[],[],[]
for docu in linkDocs: 
	print docu.PathName
	coll_rooms=FilteredElementCollector(docu).OfCategory(BuiltInCategory.OST_Rooms).ToElements()
	for r in coll_rooms:
		if r.Location != None:
			rooms.append(r)
			roomName = Element.Name.GetValue(r)
			roomNames.append("-0-" if len(roomName)==0 else roomName)
			roomNumbers.append("-0-" if len(r.Number)==0 else r.Number)
			roomAreas.append(r.Area)
			roomLocPoints.append(r.Location.Point)
roomsList = zip(roomNames,roomNumbers,roomAreas,roomLocPoints)
for room in roomsList:
	for re in room:
		print re,"-,-",
	print
	