reverse = (s) ->
  if s.length < 2 then s else reverse(s[1..-1]) + s[0]

s = "HelloWorld"
console.log "s=#{s}, s.reverse=#{reverse(s)}"
