#! /usr/bin/env lua

local cli_helpers = require("helpers.cli")
local cli_constants = require("constants.cli")
local sub_command = arg[1]

-- Install command
if sub_command == cli_constants.sub_commands[1] then
  print("WIP!")
else
  cli_helpers.send_help_text()
end
