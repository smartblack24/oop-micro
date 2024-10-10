class Desktop:

  def __init__(self) -> None:
    self.__max_price = 2000

  def sell(self):
    return f"Selling Price: {self.__max_price}"

  def setMaxPrice(self, price):
    if price > self.__max_price:
      self.__max_price = price


desktop = Desktop()
print(desktop.sell())

desktop.__max_price = 30000
print(desktop.sell())

desktop.setMaxPrice(30000)
print(desktop.sell())
