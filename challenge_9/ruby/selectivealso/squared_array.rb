require 'benchmark'

puts Benchmark.measure {

nums = Array.new(10000) {rand(-1000...1000)}

class Array
  def square
    map! {|num| num ** 2}
    sort
  end
end

puts nums.square

}
