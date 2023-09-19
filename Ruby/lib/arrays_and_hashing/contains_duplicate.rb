# frozen_string_literal: true
class Solution
  # @param {Integer[]} nums
  # @return {Boolean}
  def contains_duplicate(nums)
    hash = {}
    nums.each do |num|
      if hash.has_key? num
        return true
      end
      hash[num] = true
    end

    false
  end
end
