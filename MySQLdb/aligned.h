#define uintptr_t size_t
#define _NOT_POWER_OF_TWO(n) (((n)&((n) - 1)))
#define _UI(p) ((uintptr_t) (p))
#define _CP(p) ((char *) p)

#define _PTR_ALIGN(p0, alignment) \
((void *) (((_UI(p0) + (alignment + sizeof(void*))) \
& (~_UI(alignment - 1)))))

/* pointer must sometimes be aligned; assume sizeof(void*) is a power of two */
#define _ORIG_PTR(p) (*(((void **) (_UI(p) & (~_UI(sizeof(void*) - 1)))) - 1))

static void *_aligned_malloc(size_t size, size_t alignment) 
{
    void *p0, *p;
    if (_NOT_POWER_OF_TWO(alignment)) {
        errno = EINVAL;
        return ((void *) 0);
    }

    if (size == 0) {
        return ((void *) 0);
    }
    if (alignment < sizeof(void *)) {
        alignment = sizeof(void *);
    }

   /* including the extra sizeof(void*) is overkill on a 32-bit
      machine, since malloc is already 8-byte aligned, as long
      as we enforce alignment >= 8 ...but oh well */
    p0 = malloc(size + (alignment + sizeof(void *)));
    if (!p0) {
        return ((void *) 0);
    }
    p = _PTR_ALIGN(p0, alignment);
    _ORIG_PTR(p) = p0;
    return p;
}

static void _aligned_free(void *memblock) {
    if (memblock) {
        free(_ORIG_PTR(memblock));
    }
}


