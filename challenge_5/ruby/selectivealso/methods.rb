class Array
  # This is the same method in challenge 2
  def find_unique
    count = Hash.new(0)

    self.each do |num|
      count[num] += 1
    end

    return count.key(1)

  end
end
