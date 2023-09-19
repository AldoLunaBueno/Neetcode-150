# frozen_string_literal: true

require 'rspec'
require 'arrays_and_hashing/contains_duplicate'

describe Solution do
  before(:each) do
    @solution = Solution.new
  end
  describe ".contains_duplicate" do
    context "given an array of numbers with duplicate numbers" do
      def self.test_contains_duplicate(input)
        it "̈contains_duplicate(#{input}) returns true" do
          expect(@solution.contains_duplicate(input)).to be_truthy
        end
      end
      test_contains_duplicate [1, 1]
      test_contains_duplicate [1, 2, 3, 1]
      test_contains_duplicate [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    end

    context "given an array of numbers without duplicate numbers" do
      def self.test_distinct_numbers(input)
        it "contains_duplicate(#{input}) returns false" do
          expect(@solution.contains_duplicate(input)).to be_falsey
        end
      end
      test_distinct_numbers [1]
      test_distinct_numbers [1, 2]
      test_distinct_numbers [1, 2, 3, 4]
    end
  end
end



