import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List
 
 
def partition(data: List,
              chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]
 
 
def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    start = time.time()
    counter = {}
    for line in chunk:
        word, _, _, count = line.split('\t')
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)
    end = time.time()
    # print(f'map_frequencies({id(counter)}) took: {(end - start):.4f} seconds')
    return counter
 
 
def merge_dictionaries(first: Dict[str, int],
                       second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged
 
async def reduce_await(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = await next(it)
    else:
        value = initializer
    for element_async in it:
        element = await element_async
        value = function(value, element)
    return value

async def main(partition_size: int):
    with open('googlebooks-eng-all-1gram-20120701-a') as f:
        contents = f.readlines()
        loop = asyncio.get_event_loop()
        tasks = []
        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            for chunk in partition(contents, partition_size):
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))
 
            intermediate_results = asyncio.as_completed(tasks)
            final_result = await reduce_await(merge_dictionaries, intermediate_results)
            
            # intermediate_results = await asyncio.gather(*tasks)
            # final_result = functools.reduce(merge_dictionaries, intermediate_results)
 
            print(f"Aardvark has appeared {final_result['Aardvark']} times.")
 
            end = time.time()
            print(f'Map reduce took: {(end - start):.4f} seconds')
 
 
if __name__ == "__main__":
    asyncio.run(main(partition_size=60000))