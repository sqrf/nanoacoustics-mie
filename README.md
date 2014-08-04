Nanoacoustic vibrations
=================



This program is designed to calculate the frequency of the acoustic vibrations of metallic nanoparticles (sizes between 0.6 -  50nm) embed in glass, water and air. The nanoparticles in this code are represented by spheres.  To get the frequencies, we use the cross section calculated with Mie's theory and then replace the static radius of the sphere with a time-dependent radius. This conduces to get the time-dependent optical transmission that coincide with the experimental parameter ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%5CDelta%20T%20/%20T) presented by some authors [1]( http://www.ncbi.nlm.nih.gov/pubmed/20411965), [2](http://scitation.aip.org/content/aip/journal/jcp/110/23/10.1063/1.479089?ver=pdfcov).



 Please see the **Theory** section at the bottom for a more extense  explanation of how this code is supported.
 
Requirements
================= 

You must have installed Python in your PC or Unix based OS, in specific the  Python- [Anaconda](https://store.continuum.io/cshop/anaconda/)  2.7 distribution . It's recomendable to have some Integrated Development Environment (IDE) used for programming in Python such as PyCharm.  It provides code analysis, graphical debugger, integrated unit tester.
 
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
When the script `runVIBRATION` is run this will display a first graph that corresponds to the wavelength dependent Transmission and where you can see the position of the plasmonic resonance. When you close this plot, automatically it will be displayed the a second plot corresponding to the vibration. This last plot shows the time dependendent transmission and from this you can see the time domain of the vibration. This plots and their corresponding data are saved in the folder `output` that is located inside the `Scripts` folder. And every time you run the code, the data and plots will be updated in this folder.
Also you can see in every running of the code data as the resonance wavelength value, the complex frequency and their magnitude, real part, imaginary part and the effective damping time of the vibration.






Theory
================= 
When electromagnetic radiation interact with matter occurs different things depending if it is a metal or a dielectric material. In this case we consider metalic nanoparticles and when electromagnetic radiation interacts with them the electromagnetic field is in some part scattered and in the rest is absorbed. This phenomenon is analogous to the classic case of a a electromagnetic wave interacting with a  thin metallic plate. In a plate the electromagnetic radiation is in part reflected and in part transmited, and the amounts that measure it are the Fresnel coefficients. In the next  we propose for particles a optical transmission coefficient with help of the scattering cross section of Mie's Theory:

 ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Csigma_%7Bscat%7D)  
 

It is important to establish that although in experimental processes this particles are not perfect spheres, in this theoritcal model we consider them as perfect spheres which imply symetry and simplifies the calculations. This model is based in a single particle embed in a medium as glass. To garantize a single particle is really hard, so the close case is experimentally work whit low concentrations of particles, so that they are so far each other.



To get an expression for the optical transmission we consider the rate of the incident electromagnetic energy intensity of field and the outgoing intensity.

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20T%3D%5Cfrac%7BI%28%5Comega%29%7D%7BI_%7Binc%7D%28%5Comega%29%7D)

 also taking into account the relationship between the cross section and the intensity of electromagnetic energy 
  ![equation](http://latex.codecogs.com/gif.latex?I%28%5Comega%29%3D%5Cfrac%7BI_%7Binc%7D%7D%7BA%7D%5Csigma_%7Bscat%7D%3D%5Cfrac%7BI_%7Binc%7D%7D%7B%5Cpi%20r_0%5E2%7D%5Csigma_%7Bscat%7D).
  
  In the last we realize that the optical transmission T is proportional to a cross section :

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20T%3D%5Cfrac%7BI%28%5Comega%29%7D%7BI_%7Binc%7D%28%5Comega%29%7D%3D%5Cfrac%7B%5Csigma_%7Bscat%7D%7D%7B%5Cpi%20r_0%5E2%7D) 

In this way we have explicitly that:

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20T%3D%5Cfrac%7BI%28%5Comega%29%7D%7BI_%7Binc%7D%28%5Comega%29%7D%3D%5Cfrac%7B%201%7D%7B%5Cpi%20r_0%5E2%7D%20%5Cfrac%7B2%5Cpi%7D%7Bk%5E2%7D%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%282n&plus;1%29%5Cleft%28%20%7C%20a_%7Bn%7D%7C%5E2&plus;%7C%20b_%7Bn%7D%7C%5E2%5Cright%29).

In the last equations we note that intensity of electromagnetic energy and hence the optical transmission are dependet of the incident electromagnetic field frequency  but they are not time dependent. That transmission corresponds to the case of a static sphere.

To build a time dependent transmission we consider not a static sphere radius but a oscillating radius as:
![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20r%28t%29%3Dr_0&plus;u%28t%29) where ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20u%28t%29) is the radial displacement , ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20r_0) is the rest radius.
Also ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20u%28t%29) is the transversal a solution of the Navier equation for a elastic sphere in a isotropic elastic medium.


Solving the navier equation for a elastic sphere

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cmu%20%5Cnabla%5E2%20%5Cvec%7Bu%7D&plus;%5Cleft%28%20%5Clambda&plus;2%5Cmu%20%5Cright%29%20%5Cnabla%20%5Cleft%28%5Cnabla%20%5Ccdot%20%5Cvec%7Bu%7D%20%5Cright%29%3D%20%5Crho%20%5Cfrac%7B%5Cpartial%5E2%20%5Cvec%7Bu%7D%7D%7B%5Cpartial%20t%5E2%7D)

we find that the solution for the time dependen radius is

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20r%28t%29%3D%20r_0%20-j_1%28s%29e%5E%7B-i%5Comega_%7Bvib%7Dt%7Dk%3Dr_0%20&plus;%5Cleft%28%20%5Cfrac%7Bcos%28s%29%7D%7Bs%7D-%5Cfrac%7Bsin%28s%29%7D%7Bs%5E2%7D%5Cright%29e%5E%7B-i%5Comega_%7Bvib%7Dt%7D)

where ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20s)  is a complex number determined by the boundary conditions ( continuity in displacement and radial stress in Navier equation), ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20k)  is the wave vector of the acoustic wave produced, ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%24%5Comega_%7Bvib%7D%24) is the frequency of the acoustic vibration, ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20%24C_%7BLI%7D%24) is the longitudinal velocity of the sound inside the nanoparticle and ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20j_1) is the first kind Bessel and fist order Bessel function.

Substituting the time dependent radius 
 
 ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20r%28t%29) instead the static radius
 ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20r_0)  in the expression for transmission we have then
 
 ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20T%3D%5Cfrac%7B%201%7D%7B%5Cleft%28%20r_0%20&plus;%5Cleft%28%20%5Cfrac%7Bcos%28s%29%7D%7Bs%7D-%5Cfrac%7Bsin%28s%29%7D%7Bs%5E2%7D%5Cright%29e%5E%7B-i%5Comega_%7Bvib%7Dt%7D%5Cfrac%7B%5Comega_%7Bvib%7D%7D%7BC_%7BLI%7D%7D%5Cright%29%5E2%7D%20%5Cfrac%7B2%7D%7Bk%5E2%7D%5Csum_%7Bn%3D1%7D%5E%7B%5Cinfty%7D%282n&plus;1%29%5Cleft%28%20%7C%20a_%7Bn%7D%7C%5E2&plus;%7C%20b_%7Bn%7D%7C%5E2%5Cright%29)
 
 this gives us a transmission in function of known parameters
 
 ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20T%3DT%28r_0%2C%20t%2C%20C_%7BLI%7D%2CC_%7BTE%7D%2CC_%7BLE%7D%2CC_%7BTE%20%7D%2C%5Crho_%7BI%7D%2C%5Crho_%7BE%7D%2CN_E%2C%20N_I%29)
 
 There's is also a refraction index dependence  ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20N_I) (inside of nanoparticle) and ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20N_E) (exterior of nanoparticle) which appear in the  coefficients ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20a_n%3Da_n%28N%29) and ![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20b_n%3Db_n%28N%29%24),  where

![equation](http://latex.codecogs.com/gif.latex?%5Cinline%20N%3D%5Cfrac%7BN_I%7D%7BN_E%7D)
 are result of Mie's theory.
 
  


================= 
