import pytest
from areator.shapes import Circle, Triangle, ShapeFactory

@pytest.mark.parametrize('radius, expected_area',
                    [
                        (1, 3.14),
                        (2.5, 19.63)]
                        )
def test_correct_circle(radius, expected_area):
    circle = Circle(radius)
    assert circle.radius == radius, "Unexpected radius value"
    assert circle.area() == pytest.approx(expected_area, 0.01), (
        "Unexpected area value")

@pytest.mark.parametrize('a, b, c, is_right, expected_area',
                    [
                        (4, 5, 6, False, 9.92),
                        (3, 4, 5, True, 6),
                        (4.5, 6, 7.5, True, 13.5),
                     ])
def test_correct_triangle(a, b, c, is_right, expected_area):
    triangle = Triangle(a, b, c)
    assert triangle.a == a, "Unexpected a-side value"
    assert triangle.b == b, "Unexpected b-side value"
    assert triangle.c == c, "Unexpected c-side value"
    assert triangle.is_right_triangle() == is_right, (
        "Unexpected right-triangle definition")
    assert triangle.area() == pytest.approx(expected_area, 0.01), (
        "Unexpected area value")


@pytest.mark.parametrize('radius, expected_exception',
                         [
                             (0, ValueError),
                             (-5, ValueError),
                             (-12.1, ValueError),
                             ('hello', TypeError),
                             ('65', TypeError),
                             ([1], TypeError)
                         ])
def test_incorrect_cicle(radius, expected_exception):
    with pytest.raises(expected_exception):
        Circle(radius)

@pytest.mark.parametrize('a, b, c, expected_exception',
                         [
                             (0, 4, 5, ValueError),
                             (4, 0, 4, ValueError),
                             (6, 6, 0, ValueError),
                             (-2, 1, 5, ValueError),
                             (4, -6, 4, ValueError),
                             (6, 6, -6, ValueError),
                             (1, 2, 3, ValueError),
                             (1.5, 2.5, 4.0, ValueError),
                             (1, 2, 'hello', TypeError),
                             (63, 64, '65', TypeError),
                             ([1], [2], [3], TypeError)
                         ])
def test_incorrect_triangle(a, b, c, expected_exception):
    with pytest.raises(expected_exception):
        Triangle(a, b, c)


def test_shape_factory():
    some_shape = ShapeFactory.create_shape(5)
    assert isinstance(some_shape, Circle), "Unexpected shape"
    assert some_shape.area() == Circle(5).area(), "Unexpected area"
    some_shape = ShapeFactory.create_shape(3, 4, 5)
    assert isinstance(some_shape, Triangle), "Unexpected shape"
    assert some_shape.area() == Triangle(3, 4, 5).area(), "Unexpected area"
    with pytest.raises(ValueError):
        ShapeFactory.create_shape(2, 3)
