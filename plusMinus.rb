#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.

def plusMinus(arr)
  # Write your code here
  count_zero = 0
  count_positive = 0
  count_negative = 0
  (0..arr.length).each do |i|
    if (arr[i]).zero?
      count_zero += 1
    elsif (arr[i]).positive?
      count_positive += 1
    elsif (arr[i]).negative?
      count_negative += 1
    end

    puts count_positive/arr.length
    puts count_negative/arr.length
    puts count_zero/arr.length

  end
end
n = gets.strip.to_i
arr = gets.rstrip.split.map(&:to_i)

plusMinus arr
