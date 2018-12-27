# Triangles Containment Problem

The problem's page is [this](https://projecteuler.net/problem=102). The challenge is to count how many triangles in a list cointain the origin. Those triangles are defined by triples of points.

## Explaining the algorithm

The solution implemented here is to use vector to determine if a point is at the right side ou at the left size of a line.

When we subtract two point, the result is a vector. This process is shown below:

![vector by point subtraction](https://docs.unity3d.com/uploads/Main/VectorSubtract.png)

Having a vector, it is realy easy to get another vector that is orthogonal to the one we have. Let's say we have a vector `v = (x y)`. The vector `w = (y -x)` is orthogonal to `v`. Another important thing to know about is that in a orthonormal plain we can calculate the dot product between two vector in two different ways: one is with the formula `v.w = ∑ vi * wi`, with `i` going from 1 to the vectors dimention. The second one is with the formula `||v|| * ||w|| * cos(ø)`, being `ø` the angles between those vectors. The first formula is important because it allows us to calculate the dot product without knowing the angle between they. The second one is important because it allows us to take conclusions about the angle between they when we have the product's value. Once modules are always positive, if the dot product is negative it means the cos is negative. If the cos is negative, the angle is bigger than 90 degrees.

Using the information above, we can take two of the points that define a triangle (for instance, `A - B`) and subtract tem to get a vector `w`. Then we can get a `v` vector that is orthogonal to `w` and points to the internal side of the triangle. In sequence we calculate another vector `z = P - B`, being `P` the point we want to check if inside the triangle or not. So we calculate the dot product between `v` and `z`. If it is positive, it means the point `P` is on right side of the `AB` line. If we see that this is true for all the three sides of the triangle (`AB`, `BC`, `CA`), the point is inside the triangle.

The extra thing we have to worry about is how the points are sorted. This is important bacause it determines if the orthonal vector will point to the internal or external side of the triangle. To solve this, I sorted them using the [atan2](https://en.wikipedia.org/wiki/Atan2) function as comparision.

The implemented algorithm could be easily adapted to work with any convex polygon, but won't work to concave ones.

## The answer

After running `python main.py 102` in the root of the project, we can see that the answer is `228`.
