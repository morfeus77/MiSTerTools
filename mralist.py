import os
directory = os.getcwd()
setnamedict = {}
missinginfodict = {}
parsed = 0
errors = 0
setname = ""
rbfname = ""
zipname = ""
    
for subdir, dirs, files in os.walk(directory):
  for file in files:
     filename = os.fsdecode(file)
     if filename.endswith(".mra"): 
        #print("Filename:",filename)
        in_file = open(os.path.join(subdir,file), 'r')
        for line in in_file:
          if "<setname>" in line:
              line = line.replace('<setname>','')
              setname = line.replace('</setname>','')
              setname = setname.lstrip()
              setname = setname.rstrip("\n")
              #print("SET: ",setname)

          if "<rbf>" in line:
              line = line.replace('<rbf>','')
              rbf = line.replace('</rbf>','')
              rbfname = rbf.lstrip()
              rbfname = rbfname.rstrip("\n")
              #print("RBF: ",rbfname)
          
          if "zip=" in line:
             array = line.split("zip=\"")
             for word in array:
                if ".zip" in word:
                  if "\'" in word:
                    array2 = word.split("\'")
                  else:
                    array2 = word.split("\"")             
                  for word2 in array2:
                     if ".zip" in word2:
                       if not ">" in word2:
                         #print("ZIP: ",word2)
                         zipname = word2
                         break
                  break 
     else:
         continue
     if setname and rbfname:
            if not setnamedict.get(setname):
                   setnamedict.setdefault(setname, [])
                   setnamedict[setname].append(rbfname)
                   parsed += 1
                   if zipname:
                     setnamedict[setname].append(zipname)
     else:                       
        if not missinginfodict.get(filename):
           errors += 1
           if not setname:
             missinginfodict[filename] = "Missing set name."
           if not rbfname:
             missinginfodict[filename] = "Missing rbf name."             
     setname = ""
     rbfname = ""
     zipname = ""
#print(setnamedict)


if parsed > 0:
  print("Parsed %i MRA files." % (parsed))

if errors > 0:
  print("Found %i MRA files with missing information." % (errors))

if parsed > 0:
  print("Writing file mra_parsed_list.csv ...")
  csvfile = open('mra_parsed_list.csv', mode='wt', encoding='utf-8')
  for setnames, values in setnamedict.items():
     if 1 < len(values):
       csvline = (setnames +";"+values[0]+";"+values[1]+"\n") 
     else:
       csvline = (setnames+";"+values[0]+"\n")  
     csvfile.write(csvline)
  csvfile.close

print("Writing file mra_error_list.csv...")

if errors > 0:
  csvfile2 = open('mra_error_list.csv', mode='wt', encoding='utf-8')

  for mranames, values in missinginfodict.items():
       csvline2 = (mranames+";"+values+"\n")  
       csvfile2.write(csvline2)
  csvfile2.close


