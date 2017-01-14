class UniqueFinder
  def initialize array
    @array = array
  end

  def find_unique
    counts.key(1)
  end

  private

  attr_reader :array

  def counts
    array.each_with_object(Hash.new(0)) { |element, hash| hash[element] += 1 }
  end
end
