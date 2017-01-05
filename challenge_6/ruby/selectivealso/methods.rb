class Array

  def start_of_range count
    if self[count - 1] + 1 != self[count]
      return true
    end
    return false
  end

  def end_of_range count
    if self[count + 1] - 1 != self[count]
      return true
    end
    return false
  end

end