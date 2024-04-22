def throw_me_an_error():
  val1 = 14
  val2 = 0
  try:
    return val1 / val2
  except Exception as e:
    print("Error:", e)

throw_me_an_error()