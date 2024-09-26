local utils = require("helpers.utils")
local constants = require("constants.cli")

local cli = {}

function cli.send_empty_line(times)
  local times = times or 1
  for _ = 1, times, 1 do
    print("")
  end
end

function cli.send_divisor()
  local _, cols = utils.get_terminal_size()
  local divisor = "="

  for _ = 1, cols / 2.5, 1 do
    divisor = divisor .. "-="
  end

  if #divisor > cols then
    divisor = string.sub(divisor, 1, -3)
  end

  cli.send_centralized(divisor)
end

function cli.send_centralized(text)
  local _, cols = utils.get_terminal_size()
  local result = text

  for _ = 1, (cols - #text) / 2, 1 do
    result = " " .. result
  end

  print(result)
end

function cli.send_help_text()
  -- Program banner
  cli.send_divisor()
  cli.send_empty_line()
  cli.send_centralized("PurePKG")
  cli.send_centralized("A simplified and fastly package manager for everyone.")
  cli.send_empty_line()
  cli.send_divisor()

  cli.send_empty_line(2)

  -- Printing all sub commands and your own description
  print("Sub Commands:")
  for i = 1, #constants.sub_commands, 1 do
    local sub_command = constants.sub_commands[i]
    print(string.format("\t%s\t\t%s", sub_command.name, sub_command.description))
  end
end

return cli
