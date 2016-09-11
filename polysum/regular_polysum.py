  import math

  def regular_polygon_area(number_of_edges, edge_length):
      """
      Regular polygon area function.

      Inputs: n, the number of edges of the regular polygon, int;
              s, the polygon edge length, float.
      Returns the regular polygon area as float
      """
      return (0.25 * n * s ** 2) / math.tan(math.pi / n)

  def regular_polygon_perimeter(number_of_edges, edge_length):
      """
      Regular polygon perimeter function.

      Inputs: n, the number of edges of the regular polygon, int;
              s, the polygon edge length, float.
      Returns the regular polygon perimeter as float.
      """
      return n * s

  def polysum(number_of_edges, edge_length):
      """
      Polysum function.

      Inputs: n, the number of edges of the regular polygon, int;
              s, the polygon edge length, float.
      Returns the sum of regular polygon area
      and the square of its perimeter rounded to 4 decimal places.
      """
      return round(regular_polygon_area(n, s) +
                   regular_polygon_perimeter(n, s) ** 2, 4)