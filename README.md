# The Universal Bar: Text-to-Fraction Encoder

A Python implementation of the "Single Cut" mathematical thought experiment. This algorithm converts any string of text—including Emojis and complex Unicode scripts—into a single, precise rational number (Fraction).

This came about when I watched a Tiktok discussing the problem. While you can't do this in reality, you can theoretically calculate the would-be fraction in a computer!

# The Concept

Imagine a metal bar exactly 1 meter long, representing the number range [0,1]. Information theory posits that any finite amount of information (a word, a book, or a library) can be represented by a single specific point on this bar.

If you cut the bar at exactly that coordinate, the length of the left piece represents your data.

1. Encoding: The code converts text into a stream of integers, pads them, and treats them as a decimal expansion (e.g., 0.00072...).
2. The Fraction: Because floating-point math lacks the precision for long strings, this program converts that decimal into an exact numerator / denominator pair using arbitrary-precision integers.
3. Decoding: It reverses the process via long division to recover the original Unicode characters.

# Some Examples

Using this sample text:
> Hi 🤖! (こんにちは)

It creates this decimal (with 7 char padding thanks to emojis):
> 0.0000072000010500000320129302000003300000320000040001237100124350012395001238500123990000041

With this as the numerator:
> 72000010500000320129302000003300000320000040001237100124350012395001238500123990000041
>> seventy-two septvigintillion, ten quinvigintillion, five hundred quattuorvigintillion, three hundred and twenty duovigintillion, one hundred and twenty-nine unvigintillion, three hundred and two vigintillion, three octodecillion, three hundred septdecillion, three hundred and twenty quindecillion, forty tredecillion, one duodecillion, two hundred and thirty-seven undecillion, one hundred decillion, one hundred and twenty-four nonillion, three hundred and fifty octillion, twelve septillion, three hundred and ninety-five sextillion, one quintillion, two hundred and thirty-eight quadrillion, five hundred trillion, one hundred and twenty-three billion, nine hundred and ninety million and forty-one

And this as the denominator:
> 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>> ten novemvigintillion

*very big numbers!*

## A simpler example: Hello World!

Now since we're dealing with a lot simpler example, with no emojis, we can survive using a padding of just three characters.

Text:
> Hello World!

Decimal:
> 0.072101108108111032087111114108100033

Numerator:
> 72101108108111032087111114108100033
>> seventy-two decillion, one hundred and one nonillion, one hundred and eight octillion, one hundred and eight septillion, one hundred and eleven sextillion, thirty-two quintillion, eighty-seven quadrillion, one hundred and eleven trillion, one hundred and fourteen billion, one hundred and eight million, one hundred thousand and thirty-three

Denominator:
> 1000000000000000000000000000000000000
>> one undecillion

All in all, very fun thought experiment to *think about*
