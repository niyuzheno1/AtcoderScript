type clay%1.cpp | clay > .\%1\main.cpp 
cd .\%1
cl.exe /I C:\Users\zachn\OneDrive\Documents\include /Zi /EHsc /D DEBUG /Fe: main.exe main.cpp