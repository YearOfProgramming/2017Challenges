import unittest
import time
import random
from FindTheDifference import Solution

class OutcomesTest(unittest.TestCase):

	#	Simple test cases for this problem

	def test_case1(self):
		case1in = Solution()
		t1 = time.time()
		case1out = case1in.findTheDifference("abcd","abcde")
		t2 = time.time()
		print 'Runtime of Case1: ' + str(t2-t1) + ' seconds' 
		self.assertEqual( case1out, 'e' )

	def test_case2(self):
		case2in = Solution()
		t1 = time.time()
		case2out = case2in.findTheDifference("abcd","dcabe")
		t2 = time.time()
		print 'Runtime of Case2: ' + str(t2-t1) + ' seconds' 
		self.assertEqual( case2out, 'e' )

	def test_case3(self):
		case3in = Solution()
		t1 = time.time()
		case3out = case3in.findTheDifference("abcdefghijklmno","abcdefghijklmnop")
		t2 = time.time()
		print 'Runtime of Case3: ' + str(t2-t1) + ' seconds' 
		self.assertEqual( case3out, 'p')

	def test_case4(self):
		case4in = Solution()
		t1 = time.time()
		case4out = case4in.findTheDifference(" ", " ")
		t2 = time.time()
		print 'Runtime of Case4: ' + str(t2-t1) + ' seconds' 
		self.assertEqual( case4out, None)

	def test_case5(self):
		finalTestStringS = 'yipsqffxmqafnrlnkwrnvspeekejbsuuvuhanlxmgkyjlgmloxmpyxuvqeabmycqycwkzvhyviaavwryyhtepqacfuzggcoctviibhbcwzmkbsivtjywienaojkcekvgsyylliasczuzoivipcsqknbshavzwyufkeaxjiunbyiuvxvpfokrfphcxbaljktkiygrboihqczhxnreigzhsinustzzrzstbpkfrqsenhrnkrfbekfwaozenxqabbhhsaxyrubmtzmvtclatncfkkvplvuwzfggfnprinyjblutbovtmxxvacouiwgrkgjvszkwswvnwaggsiwzymixwmhmujmuckgyiwcwrigtshqeuguytpjjsrmijmxikeraqqgjymbvmvcugxubuxmlzoiqzfjwpzpqnwalcxczzxaitpmjsorwzmwzgjcgpztaynujqqmhvyscupqjflrnjqseeapavmakvexuvkntgcvkvonjqoivimybahutpjtzubamihhbyhspgtmjwexylkqqjvmtpxxcjnlpbkaiiekjlxkrewthipzhfljcfyuclowlptfhksrngxpzijabhfjhwtlbfuouqskheybgoqinmhnjzciqvscvneokfqrghekuzkahlyosemcgqipimjaypxkkwvtqztcexlhogjqfxvfihqqcriaimioaezfrbaxwfuwbiylpztmxovutxwhqrlrxfwpfcppazjsztewupvarsqcizlneiomljrbufbuhljmgnlqkofsersqhfucsvfswqxnmqlthjcopeaseqmsghvqpnmxmuvuoteoqsaneknirsjrleslfsiceoypypbijhmtmesxpxcurnxjzwjclcesyfmffbcsxvnlhtnmwgxaywahyhqqfuevmwhhovxrqsslemlpxeiuqipmtqmeqosghyvgyexblvnsbofvtjqfhcowmfvhyyerktinhggqamtykvntxyywn'
		finalTestStringT = ''.join(random.sample(finalTestStringS,len(finalTestStringS)))
		finalTestStringT += 'p'
		case5in = Solution()
		t1 = time.time()
		case5out = case5in.findTheDifference( finalTestStringS, finalTestStringT + 'p')
		t2 = time.time()
		print 'Runtime of Case5: ' + str(t2-t1) + ' seconds' 
		self.assertEqual( case5out, 'p')

if __name__ == '__main__':
	unittest.main()