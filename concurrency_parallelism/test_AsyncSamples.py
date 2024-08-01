import asyncio
from unittest import TestCase

from concurrency_parallelism.AsyncSamples import AsyncSamples

class TestAsyncSamples(TestCase):
    def test_main(self):
        async_sample = AsyncSamples()
