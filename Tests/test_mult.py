import unittest

from fraction import Fraction


class TestFractionMultiplication(unittest.TestCase):
    """Test cases for the Fraction.__mul__ method."""

    def test_mul_two_fractions_basic(self):
        """Test multiplying two basic fractions."""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        result = f1 * f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 8)

    def test_mul_fractions_result_simplifies(self):
        """Test that multiplication result is normalized to lowest terms."""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_mul_fraction_by_one(self):
        """Test multiplying a fraction by 1 (Fraction(1, 1))."""
        f = Fraction(5, 7)
        result = f * Fraction(1, 1)
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 7)

    def test_mul_fraction_by_zero(self):
        """Test multiplying a fraction by 0 (Fraction(0, 1))."""
        f = Fraction(5, 7)
        result = f * Fraction(0, 1)
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

    def test_mul_fraction_by_integer(self):
        """Test multiplying a fraction by an integer."""
        f = Fraction(3, 4)
        result = f * 2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 2)

    def test_mul_fraction_by_zero_integer(self):
        """Test multiplying a fraction by integer 0."""
        f = Fraction(5, 7)
        result = f * 0
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

    def test_mul_fraction_by_one_integer(self):
        """Test multiplying a fraction by integer 1."""
        f = Fraction(5, 7)
        result = f * 1
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 7)

    def test_mul_fraction_by_negative_fraction(self):
        """Test multiplying a positive fraction by a negative fraction."""
        f1 = Fraction(1, 2)
        f2 = Fraction(-3, 4)
        result = f1 * f2
        self.assertEqual(result.numerator, -3)
        self.assertEqual(result.denominator, 8)

    def test_mul_two_negative_fractions(self):
        """Test multiplying two negative fractions."""
        f1 = Fraction(-1, 2)
        f2 = Fraction(-3, 4)
        result = f1 * f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 8)

    def test_mul_by_negative_integer(self):
        """Test multiplying a fraction by a negative integer."""
        f = Fraction(1, 2)
        result = f * -3
        self.assertEqual(result.numerator, -3)
        self.assertEqual(result.denominator, 2)

    def test_mul_commutative_property(self):
        """Test that multiplication is commutative: a * b == b * a."""
        f1 = Fraction(2, 5)
        f2 = Fraction(3, 7)
        result1 = f1 * f2
        result2 = f2 * f1
        self.assertEqual(result1.numerator, result2.numerator)
        self.assertEqual(result1.denominator, result2.denominator)

    def test_mul_associative_property(self):
        """Test that multiplication is associative: (a * b) * c == a * (b * c)."""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        f3 = Fraction(3, 4)
        result1 = (f1 * f2) * f3
        result2 = f1 * (f2 * f3)
        self.assertEqual(result1.numerator, result2.numerator)
        self.assertEqual(result1.denominator, result2.denominator)

    def test_mul_large_numerators_and_denominators(self):
        """Test multiplication with large numbers that simplify."""
        f1 = Fraction(100, 200)
        f2 = Fraction(50, 100)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

    def test_mul_produces_fraction_object(self):
        """Test that multiplication returns a Fraction object."""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 * f2
        self.assertIsInstance(result, Fraction)

    def test_mul_does_not_modify_operands(self):
        """Test that multiplication does not modify either operand."""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        f1_num_before = f1.numerator
        f1_den_before = f1.denominator
        f2_num_before = f2.numerator
        f2_den_before = f2.denominator

        _ = f1 * f2

        self.assertEqual(f1.numerator, f1_num_before)
        self.assertEqual(f1.denominator, f1_den_before)
        self.assertEqual(f2.numerator, f2_num_before)
        self.assertEqual(f2.denominator, f2_den_before)

    def test_mul_fractions_with_common_factors(self):
        """Test multiplication where common factors exist across operands."""
        f1 = Fraction(4, 9)
        f2 = Fraction(6, 8)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 3)

    def test_mul_identity_element(self):
        """Test that multiplying by 1 acts as identity element."""
        f = Fraction(7, 11)
        result = f * 1
        self.assertEqual(result.numerator, f.numerator)
        self.assertEqual(result.denominator, f.denominator)

    def test_mul_zero_absorbing_element(self):
        """Test that multiplying by 0 results in 0."""
        f = Fraction(7, 11)
        result = f * 0
        self.assertEqual(result.numerator, 0)
        self.assertEqual(result.denominator, 1)

    def test_mul_unsupported_type_raises_typeerror(self):
        """Test that multiplying by an unsupported type raises TypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            _ = f * "string"

    def test_mul_by_float_raises_typeerror(self):
        """Test that multiplying by a float raises TypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            _ = f * 3.5

    def test_mul_by_none_raises_typeerror(self):
        """Test that multiplying by None raises TypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            _ = f * None

    def test_mul_by_list_raises_typeerror(self):
        """Test that multiplying by a list raises TypeError."""
        f = Fraction(1, 2)
        with self.assertRaises(TypeError):
            _ = f * [1, 2]

    def test_mul_same_fraction(self):
        """Test multiplying a fraction by itself."""
        f = Fraction(2, 3)
        result = f * f
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 9)

    def test_mul_fraction_with_large_integers(self):
        """Test multiplication with large integers."""
        f1 = Fraction(1000, 999)
        f2 = Fraction(999, 1000)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)


if __name__ == "__main__":
    unittest.main()
