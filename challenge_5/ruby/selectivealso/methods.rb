class ElementsArray < Array

  def initialize elements, comparison
    @elements = elements.chars
    @comparisons = comparison.chars
  end

  def find_diff_chars
    count = Hash.new(0)

    @elements.each do |element|
      count[element] += 1
    end

    @comparisons.each do |comparison|
      count[comparison] += 1
    end

    count.each do |char, occurances|
      if occurances % 2 == 1
        return char
      end
    end
  end

end
