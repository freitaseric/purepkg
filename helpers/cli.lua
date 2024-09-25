local cli = {}

function cli.send_empty_line()
  print("")
end

function cli.send_divisor()
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
end

function cli.send_help_text()
  cli.send_empty_line()
  
  cli.send_divisor()
  print("PurePKG")
  print("A simplified and fastly package manager for everyone.")
  cli.send_divisor()

  cli.send_empty_line()
end

return cli