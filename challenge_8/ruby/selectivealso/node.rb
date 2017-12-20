class Node
  protected
  attr_writer :prev, :next

  public
  attr_reader :value, :prev, :next, :data, :id

  def initialize()
    @id = ('a'..'z').to_a.shuffle[0,3].join
    @data = ('a'..'z').to_a.shuffle[0,10].join
  end

  def remove
    @prev.next = @next if @prev
    @next.prev = @prev if @next
    @next = @prev = nil
  end

  def insert_after(node)
    remove

    @next = node.next
    @next.prev = self if @next
    @prev = node
    node.next = self
  end
end
