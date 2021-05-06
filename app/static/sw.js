var staticCacheName = 'djangopwa-v2';

self.addEventListener('install', function (event) {
    // event.waitUntil(
    //     caches.open(staticCacheName).then(function (cache) {
    //         return cache.addAll([
    //             '',
    //         ]);
    //     })
    // );
});

self.addEventListener('activate', function (event) {
    event.waitUntil(
        caches.keys().then(staticCacheName => {
            return Promise.all(
                staticCacheName.map(cache => {
                    if (cache !== staticCacheName) {
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
});


self.addEventListener('fetch', function (event) {
    event.respondWith(
        fetch(event.request)
            .then(res => {
                const resClone = res.clone();
                caches.open(staticCacheName)
                    .then(cache => {
                        cache.put(event.request, resClone);
                    });
                return res;
            }).catch(err => caches.match(event.request).then(res => res))
    );



    // var requestUrl = new URL(event.request.url);
    // if (requestUrl.origin === location.origin) {
    //     if ((requestUrl.pathname === '/')) {
    //         event.respondWith(caches.match(''));
    //         return;
    //     }
    // }
    // event.respondWith(
    //     caches.match(event.request).then(function (response) {
    //         return response || fetch(event.request);
    //     })
    // );
});