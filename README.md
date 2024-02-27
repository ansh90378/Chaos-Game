# Chaos-Game
The chaos game is a method to generate iterative fractals with the help of polygons.

The rules are simple and will be explained using the example of a triangle. It has the corner points A, B and C. You start the chaos game at a random point P1 within the triangle. To calculate the next position P2, you choose one of the three corner points of the triangle at random and place P2 in the middle of the route between point P1 and the randomly selected corner point. You repeat this process as often as you like and draw every point you obtain on to the screen. 

![CG(1)](https://github.com/ansh90378/Income-prediction/assets/78586456/9ef29dec-1ae5-4c4e-bc04-a4f8a5edb934)

## Generalization to arbitrary polygons
This construction mechanism for fractals can be applied to any polygon. However, if you increase the number of corners, you should no longer halve the distance, but adjust the factor slightly, otherwise the algorithm will not always create a fractal. For example: If you halve the distance between the current position and the randomly selected corner of a square you get an evenly filled area and not a fractal.
Halving the distance in a triangle corresponds to multiplying its length by a factor of 0.5. If this is generalized to polygons with n-vertices, then a favorable factor for any polygons with n-corner points can be computed with this equation: 


$$ 
  r = n / (n + 3)
$$

## Constraining the random selection of corner points
Constraints on the selection are introduced. Such constraints can include:

* A corner point must not be selected twice in succession
* If a corner point has been selected, none of its neighbors may be selected in the next step.
* If the same corner point was selected twice in succession, the corner point selected in the     next step must at least be 2 corners away.



'

    def random_point_index(p):
      global idx
      idx[2] = idx[1]
      idx[1] = idx[0]
      dst1 = abs(idx[1] - idx[2])

      while True:
          idx[0] = random.randint(0, len(p) - 1)  # Purely random selection, the rest is just applying constraints
          dst = abs(idx[0] - idx[1])
          if dst1 == 0 and (dst == 1 or dst == len(p) - 1):
              continue
          else:
              break

      return idx[0]

The function random_point_index selects a random corner point of the polygon and returns its index. For this purpose, it receives an array of polygon corner points as its input parameter. For a purely random selection of points, it would be sufficient to use the bold line. The variant shown here contains the contraint that if the same corner point was selected twice, the next corner point must not be a direct neighbor.



![CG_Result(2)](https://github.com/ansh90378/Income-prediction/assets/78586456/904d5809-5f45-417c-a4b8-b1af13cc5256)

