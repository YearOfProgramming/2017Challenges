nums = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]

class Array
  def find_unique
    count = Hash.new(0)

    self.each do |num|
      count[num] += 1
    end

    return count.key(1)

  end
end


puts nums.find_unique
