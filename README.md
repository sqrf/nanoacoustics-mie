Nanoacoustic vibrations
=================



This program is designed to calculate the frequency of the acoustic vibrations of metallic nanoparticles (sizes between 0.6 -  50nm) embed in glass, water and air. The nanoparticles in this code are represented by spheres.  To get the frequencies, we use the cross section calculated with Mie's theory and then replace the static radius of the sphere with a time-dependent radius. This conduces to get the time-dependent optical transmission that coincide with the experimental parameter ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%5CDelta%20T%20/%20T) presented by some authors [1]( http://www.ncbi.nlm.nih.gov/pubmed/20411965), [2](http://scitation.aip.org/content/aip/journal/jcp/110/23/10.1063/1.479089?ver=pdfcov).



 Please see the **Theory** section at the bottom for a more extense  explanation of how this code is supported.
 
Requirements
================= 

You must have installed python in your PC or Unix based OS. It's recomendable to have some Integrated Development Environment (IDE) used for programming in Python such as PyCharm.  It provides code analysis, graphical debugger, integrated unit tester.
 
 Using nanoacustics
================= 

To use this code, first download the .zip file and locate  all the content in a unique folder in the hard drive.
Once this is done you can open the script `runVIBRATION` from the folder `Scripts`. If you decided to use PyCharm you must create first a project and then open the script. In this script you will find a function with four input arguments:

```
param = Parameters(metal, media, tmax, radius)
```

where the first one is related to the metal and it can be Al, Au, Pt, Ag and Cu; the second paramter is related to the media in which the nanoparticle is. The media can be glass, water or air. The third parameter tmax is related to the temporal scale in which the simulation has place. Some vibrations take more time than others and you can choose the time scale in picoseconds. The last argument is related to the radius of the nanoparticle in nanometers. An example of a vibration of 0.75nm  platinum nanoparticule embed in glass with a time scale of 0.01 ps is the next:
```
param = Parameters(metals.Pt, medios.glass, 0.01, 0.75)
```

It's important to note that the metal and media always are written after the dot of the class metals and media.
When the script `runVIBRATION` is run this will display a first graph that corresponds to the wavelength dependent Transmission and where you can see the position of the plasmonic resonance. When you close this plot, automatically it will be displayed the a second plot corresponding to the vibration. This last plot shows the time dependendent transmission and from this you can see the time domain of the vibration. This plots and their corresponding data are saved in the folder `output`. And every time you run the code, the data and plots will be updated in this folder.
Also you can see in every running of the code data as the resonance wavelength value, the complex frequency and their magnitude, real part, imaginary part and the effective damping time of the vibration.






Theory
================= 
En el caso de una nanopartícula met\'alica, se asumir\'a como  esf\'erica por simplicidad y simetr\'ia. Adem\'as esta nanopart\'icula se considera aislada, sin part\'iculas vecinas pr\'oximas, evitando as\'i contribuciones \'opticas y mec\'anicas. Lo anterior est\'a en concordancia con Broyer [1]( http://www.ncbi.nlm.nih.gov/pubmed/20411965), donde se reporta que la concentraci\'on de nanopart\'iculas es lo suficientemente baja en los vol\'umenes de sustraro empleados.

\bigskip
Hacer un c\'alculo similar al de la trasmitividad o transmisi\'on \'optica para una esfera no resulta tan trivial como para una placa.  Cuando una onda electromagn\'etica incide sobre una esfera met\'alica en vez de producirse reflexi\'on y trasmisi\'on de la onda se tiene  absorbci\'on  y dispersi\'on.
Al estudio del caso de interacci\'on de radiaci\'on electromagn\'etica se le conoce propiamente como teor\'ia de Mie  la cual se abordad\'o en detalle en el capitulo 4. La teoría de Mie como tal, no proporciona una expresi\'on para la trasmisi\'on \'optica sino para la secci\'on eficaz de absorci\'on ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Csigma_%7Babs%7D )y dispersi\'on  ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Csigma_%7Bscat%7D)  de radiaci\'on electromagn\'etica.


Para obtener una expresi\'on gen\'erica de la transmisi\'on \'optica se tiene en cuenta que \'esta se puede ver como el cociente de comparar la intensidad de la energa electromagntica saliente de un material con la energa inicial incidente

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20T%3D%5Cfrac%7BI%28%5Comega%29%7D%7BI_%7Binc%7D%28%5Comega%29%7D)

 y considerando por otro la relacin existente entre las secciones eficaces y las intensidades de energa electromagntica ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20I%28%5Comega%29%3D%5Cfrac%7BI_%7Binc%7D%7D%7BA%7D%5Csigma_%7Bscat%7D%3D%5Cfrac%7BI_%7Binc%7D%7D%7B%5Cpi%20r%5E2%7D%5Csigma_%7Bscat%7D)   se tiene que la transmisi\'on \'optica  es proporcional a una seccin eficaz:

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20T%3D%5Cfrac%7BI%28%5Comega%29%7D%7BI_%7Binc%7D%28%5Comega%29%7D%3D%5Cfrac%7B%5Csigma_%7Bscat%7D%7D%7B%5Cpi%20r_0%5E2%7D) 

In this way we have explicitly that:

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20T%3D%5Cfrac%7BI%28%5Comega%29%7D%7BI_%7Binc%7D%28%5Comega%29%7D%3D%5Cfrac%7B%201%7D%7B%5Cpi%20r_0%5E2%7D%20%5Cfrac%7B2%5Cpi%7D%7Bk%5E2%7D%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%282n&plus;1%29%5Cleft%28%20%7C%20a_%7Bn%7D%7C%5E2&plus;%7C%20b_%7Bn%7D%7C%5E2%5Cright%29)

En la expresiones anteriores es de notar que la intensidad y por tanto la transmisi\'on \'optica son dependientes de la frecuencia del campo electromagntico incidente pero estas no evolucionan en el tiempo, por tanto tal transmisi\'on corresponde al caso de una esfera est\'atica dispersando luz. 
  
  \bigskip
  
  La evolucin temporal se  logra considerando un radio oscilante de la forma ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20r%28t%29%3Dr_0&plus;u%28t%29) donde ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20u%28t%29) es el desplazamiento radial, ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20r_0) es el radio en reposo y se relaciona con la expansi\'on y contracci\'on de la esfera. Asimismo ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20u%28t%29)  es soluci\'on de la ecuaci\'on de Navier aplicada a una esfera el\'astica en un medio isotr\'opico.
  En este punto es importante establecer al igual que con la placa conductoras regiones en donde se solucionara el problema. Las cantidades relacionadas con el interior de la esfera se denotaran con el sub\'indice $I$ de interior y las relacionadas con el exterior se denotaran con el sub\'indice $E$. De esta forma se tiene que el desplazamiento $u$ en la parte interna es ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20u_I) y el desplazamiento en la parte externa es ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20u_E). 
  
Solving the navier equation for a elastic sphere

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cmu%20%5Cnabla%5E2%20%5Cvec%7Bu%7D&plus;%5Cleft%28%20%5Clambda&plus;2%5Cmu%20%5Cright%29%20%5Cnabla%20%5Cleft%28%5Cnabla%20%5Ccdot%20%5Cvec%7Bu%7D%20%5Cright%29%3D%20%5Crho%20%5Cfrac%7B%5Cpartial%5E2%20%5Cvec%7Bu%7D%7D%7B%5Cpartial%20t%5E2%7D)

we find that the solution for the time dependen radius is

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20r%28t%29%3D%20r_0%20-j_1%28s%29e%5E%7B-i%5Comega_%7Bvib%7Dt%7Dk%3Dr_0%20&plus;%5Cleft%28%20%5Cfrac%7Bcos%28s%29%7D%7Bs%7D-%5Cfrac%7Bsin%28s%29%7D%7Bs%5E2%7D%5Cright%29e%5E%7B-i%5Comega_%7Bvib%7Dt%7D)

donde ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20s) es una cantidad compleja a determinarse por las condiciones de frontera, ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20k) es el vector de onda de la vibraci\'on ac\'ustica producida, ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%24%5Comega_%7Bvib%7D%24) es la frecuencia de la vibraci\'on, ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%24C_%7BLI%7D%24) es la velocidad longitudinal del sonido en el interior de la esfera (velocidad del metal en cuesti\'on)	y ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20j_1) es la funci\'on de Bessel esf\'erica de primera clase de orden uno que se escribe expl\'icitamente en la segunda igualdad.
 
 Sustituyendo el radio dependiente del tiempo ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20r%28t%29) en lugar del radio est\'atico ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20r_0)  en la expresi\'on for transmission 
 
 ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20T%3D%5Cfrac%7B%201%7D%7B%5Cleft%28%20r_0%20&plus;%5Cleft%28%20%5Cfrac%7Bcos%28s%29%7D%7Bs%7D-%5Cfrac%7Bsin%28s%29%7D%7Bs%5E2%7D%5Cright%29e%5E%7B-i%5Comega_%7Bvib%7Dt%7D%5Cfrac%7B%5Comega_%7Bvib%7D%7D%7BC_%7BLI%7D%7D%5Cright%29%5E2%7D%20%5Cfrac%7B2%7D%7Bk%5E2%7D%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%282n&plus;1%29%5Cleft%28%20%7C%20a_%7Bn%7D%7C%5E2&plus;%7C%20b_%7Bn%7D%7C%5E2%5Cright%29)
 
 this gives us a transmission in function of known parameters
 
 ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20T%3DT%28r_0%2C%20t%2C%20C_%7BLI%7D%2CC_%7BTE%7D%2CC_%7BLE%7D%2CC_%7BTE%20%7D%2C%5Crho_%7BI%7D%2C%5Crho_%7BE%7D%2CN_E%2C%20N_I%29)
 
 
 la dependencia en los \'indices de refracci\'on ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20N_I) (interior de la nanopart\'icula) y ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20N_E) (exterior de la nanopart\'icula) se tiene en los coeficientes ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20a_n%3Da_n%28N%29) y ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20b_n%3Db_n%28N%29%24),  donde

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20N%3D%5Cfrac%7BN_I%7D%7BN_E%7D)
 are result of Mie's theory.
 
  


================= 
