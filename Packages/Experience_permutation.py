sequence = [2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4, 1, 3] # ordre des personne invariantes ex: 1, 2, 3 : le 1 reste puis le 2 reste..
size_table = 4  # nombre de personne par table

table1 = ["1A", "2A", "3A", "4A"]
table2 = ["1B", "2B", "3B", "4B"]
table3 = ["1C", "2C", "3C", "4C"]
table4 = ["1D", "2D", "3D", "4D"]

tables = [list(table1), list(table2), list(table3), list(table4)]
tableau = [[list(tables[0]), list(tables[1]), list(tables[2]), list(tables[3])]]  #pour export en html

print(tables)
for i in sequence:
	jump = 0  #nombre de table à sauter (ex: le 1 reste et le 2 avance de 1, le 3 de 2 , le 4 de 3)
	for j in range(size_table):
		if j != i-1:
			jump += 1
			tables[0][j], tables[1][j], tables[2][j], tables[3][j] = tables[(0-jump)%size_table][j], tables[(1-jump)%size_table][j], tables[(2-jump)%size_table][j], tables[(3-jump)%size_table][j]
	tableau += [[list(tables[0]), list(tables[1]), list(tables[2]), list(tables[3])]]
	print(tables)

colors = {"A": "#e000e0", "B":"#27e000", "C": "#25c7e0", "D": "#ffda55"}
def export_html(L):
	html = "<!doctype html>\n"+"<html>\n"+"	<head>\n"
	html += '		<meta charset="utf-8">\n'+"	</head>\n"
	html += "	<body>\n"+'		<table border="0">\n'
	for i in L:
		html += "			<tr>\n"
		for j in i:
			for k in j:
				html += '				<td bgcolor="'+colors[k[1]]+'">'+"<pre> "+k+" </pre>"+"</td>\n"
			html += "				<td><pre>  </pre></td>\n"
		html += "			</tr>\n"
	html += "		</table>\n"+"	</body>\n"+"</html>"
	with open("export.html", "w") as fichier:
		fichier.write(html)
		
export_html(tableau)

# ouverture html :
##import ui,os
##from urllib.parse import urljoin
##import webbrowser
##file_path = "export.html"
##file_path = urljoin('file://', os.path.abspath(file_path))
##webbrowser.open(file_path)
