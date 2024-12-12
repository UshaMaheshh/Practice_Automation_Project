import logging
import os
class log_gen():
   @staticmethod
   def loggen():
      path = os.path.abspath("C:\\Users\\usha5\\PycharmProjects\\PracticeTestingProject\\logs\\automation.log")
      # print(path)
      logging.basicConfig(filename=path, format='%(asctime)s: %(levelname)s: %(message)s',
                       datefmt='%m/%d/%Y %I:%M:%S %p', force=True)


      logger = logging.getLogger('root')
      logger.setLevel(logging.INFO)
      return logger


