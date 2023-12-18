library("LIHKGr")

args <- commandArgs(trailingOnly = TRUE)

start <- args[1]
end <- args[2]

lihkg <- create_lihkg(browser = "firefox", port = sample(10000:60000, 1), verbose = FALSE);


str1 <- "./txt/lihkg_"
str2 <- "./csv/lihkg_"
csv_file <- paste0(str2, start, "-", end, ".csv")
print(csv_file)
txt_file <- paste0(str1, start, "-", end, ".txt")

lihkg$scrape(start:end)

rio::export(lihkg$bag, csv_file)

writeLines(lihkg$bag$text, txt_file)
