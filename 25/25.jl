using Base.Test

function fibonacci(n)
    if n == 1 || n == 2
        return 1
    end

    return fibonacci(n-1) + fibonacci(n-2)
end

@test fibonacci(1) == 1
@test fibonacci(2) == 1
@test fibonacci(10) == 55
@test fibonacci(12) == 144

index = 2
prev, curr = BigInt(1), BigInt(1)
while length(string(curr)) < 1000
    curr, prev = curr + prev, curr
    index+=1
end
println(index, " ", curr)
