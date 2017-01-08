class ElementsArray < Array

  def initialize elements
    @elements = elements
  end

  def find_unique
    count = Hash.new(0)

    @elements.each do |element|
      count[element] += 1
    end
    
    return count.key(1)
  end
end
