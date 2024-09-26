local utils = {}

-- A function that return the user terminal dimensions (rowsXcols)
function utils.get_terminal_size()
  local handle = io.popen("stty size")
  if handle == nil then
    return nil, nil
  end

  local result = handle:read("*a")
  handle:close()

  local rows, cols = result:match("(%d+)%s+(%d+)")
  return tonumber(rows), tonumber(cols)
end

return utils
