# Essence of linear algebra 
https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab

## content

### Chapter 1 Vectors, what even are they?
#### Vector
- root-of-all building block for linear algebra
  - **Physics**: Vectors are arrows pointing in space, the factors defining the vector are its length and the direction it is pointing, the vectors can sit anywhere they want
  - **Computer Science**: Vectors are ordered lists of numbers
  - **Mathematician**: Vectors can be anything where there is a sensible notion of adding two vectors and multiplying a vector by a number
- Vector in linear algebra 
  - An arrow, specifically an arrow inside a coordinate system (Most cases, the vector will be rooted at the origin)
  - When numbers like 2, -1.8, etc. are used to scale(缩放) some vectors, the numbers are called scalars(标量/纯良)

### Chapter 2 Linear combinations, span, and basis vectors
#### Basis vectors
- Think of each coordinate as a scalar [3, -2] = 3 * **i** + (-2) * **j**
  - **i** unit vector in the x-direction
  - **j** unit vector in the y-direction
  - **i** and **j** are the standard 'basis vectors' of the xy coordinate system
- Basis vectors for different coordinate systems 
#### Linear combination of two vectors
- linear combination of **v** and **w**
  - a **v** + b **w**
#### Span
- The span of **v** and **w** is the set of all their linear combinations
- The span of two vectors (in different direction) in 3-dimensional space is a flat sheet
- The span of three vectors (in different direction) in 3-dimensional space is the full three dimensions of space
#### Vectors as points
- When dealing with collections of vectors, it is common to represent each one with just a point in space
  - Think of individual vectors as arrow.
  - Think of sets of vectors as points.
#### Linearly dependent
- One of the vectors can be expressed as a linear combination of the others since it is already in the span of the others
#### Linearly independent
- If each vector really does add another dimenssion to the span, they are said to be linearly independent

### Chapter 3 Matrices as linear transformations ***important***
#### Linear transformation
- transformation (more vivid for describing the movement of the vectors) 
  - a fancy word for 'function' that takes in inputs and spits out an output for each one
- linear means:
  - all lines remains lines without getting curved 
  - the origin must remain fixed in place
- Think of linear transformation as keeping grid lines parallel and evenly spaced
#### Matrix multiplication
- 2 * 2 matrix  (a matrix can be seen as a certain transformation of space)
  ```
  [a b] [x]  -->  x[a] + y[b] --> [ax + by]    the first column (a,c) is the place where the first basis vector lands
  [c d] [y]  -->  x[c] + y[d] --> [cx + dy]    the second column (b,d) is the place where the second basis vector lands
  ```
- Matrix multiplication is just a way to compute what that transformation does to a given vector

### Chapter 4 Matrix multiplication as composition
####
####
